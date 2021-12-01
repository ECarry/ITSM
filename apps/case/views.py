from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import View
from .forms import CaseForm
from .models import *
from apps.user.mixin import LoginRequiredMixin
from django.core.paginator import Paginator


# 新建工单视图 form
class NewCaseFormView(LoginRequiredMixin, View):
    def get(self, request):
        form = CaseForm()

        context = {
            'form': form
        }

        return render(request, 'new_case_form.html', context)

    def post(self, request):
        # 当前登录用户
        current_user = request.user

        # 初始化值，无需用户键入的值
        case_detail = Case(register_id=current_user.id)

        form = CaseForm(request.POST, instance=case_detail)
        if form.is_valid():
            form.save()
            return redirect('case:case_list')
        else:
            context = {
                'form': form
            }
            return render(request, 'new_case_form.html', context=context)


# 工单列表视图
class CaseView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取所有工单
        case_all = Case.objects.all()

        # 分页显示
        # https://docs.djangoproject.com/zh-hans/3.2/ref/paginator
        paginator = Paginator(case_all, 10)     # 每页10个
        page_num = request.GET.get('page', 1)  # 获取分页码
        page_of_cases = paginator.get_page(page_num)

        context = {
            'cases': page_of_cases,
                   }

        return render(request, 'case.html', context)


# 工单详情视图
class CaseDetailView(LoginRequiredMixin, View):
    def get(self, request, case_pk):
        # 获取单个工单，id
        case = get_object_or_404(Case, pk=case_pk)
        context = {
            'case': case
        }

        return render(request, 'case_detail.html', context)


# 新建项目
class NewProjectView(LoginRequiredMixin, View):
    # get 显示新建项目页面
    def get(self, request):
        # 获取客户名称
        company = Company.objects.all()

        context = {
            'company': company
        }

        return render(request, 'new_project.html', context)

    # post 新建项目
    def post(self, request):
        project_num = request.POST.get('project_num')

        # 判断是否已存在项目
        try:
            p = Project.objects.filter(project_num=project_num)
        except Project.DoesNotExist:
            # 项目不存在
            p = None

        if p:
            return render(request, 'new_project.html', {'errmsg': "项目编号" + " " + project_num + " " +
                                                        "已存在", 'error_show': "show"})

        # 获取并处理 POST 数据
        info = request.POST.dict()
        del info['csrfmiddlewaretoken']

        # 写入数据库
        Project.objects.create(**info)
        return redirect('case:project_list')
        # # 获取用户输入信息
        # project_name = request.POST.get('project_name')
        #
        # contract_num = request.POST.get('contract_num')
        # start_time = request.POST.get('start_time')
        # end_time = request.POST.get('end_time')
        # company = request.POST.get('company_id')
        #
        # # 判断数据是否完整
        # if not all([project_name, project_num, contract_num, start_time, end_time, company]):
        #     return render(request, 'project.html', {'errmsg': "数据不完整"})
        #

        # # 保存数据
        # Project.objects.create(name=project_name,
        #                        project_num=project_num,
        #                        contract_num=contract_num,
        #                        start_time=start_time,
        #                        end_time=end_time,
        #                        company_id=company)
        #
        # return render(request, 'new_project.html', {'msg': "项目创建成功", 'success_show': "show"})


# 项目视图
class ProjectView(LoginRequiredMixin, View):
    def get(self, request):
        projects = Project.objects.all()

        # 分页显示
        paginator = Paginator(projects, 10)     # 每页显示10个
        page_num = request.GET.get('page', 1)
        page_of_projects = paginator.get_page(page_num)

        context = {
            'projects': page_of_projects
        }
        return render(request, 'project.html', context)


# 项目详细视图
class ProjectDetailView(LoginRequiredMixin, View):
    # get 显示项目详情
    def get(self, request, project_pk):
        # id 获取单个项目详情
        project = get_object_or_404(Project, pk=project_pk)

        # 获取客户公司
        companys = Company.objects.all()

        context = {
            'project': project,
            'companys': companys
        }

        return render(request, 'project_detail.html', context)

    # post 更新项目
    def post(self, request, project_pk):
        info = request.POST.dict()
        del info['csrfmiddlewaretoken']
        print(info)
        project = Project.objects.filter(id=project_pk)
        project.update(
            **info
        )

        return redirect('case:project_list')
