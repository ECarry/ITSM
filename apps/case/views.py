from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import View
from .models import *
from apps.user.mixin import LoginRequiredMixin


# 工单视图
class CaseView(LoginRequiredMixin, View):
    def get(self, request):
        # 获取所有工单
        context = {'cases': Case.objects.all()}

        # 分页显示

        return render(request, 'case.html', context)


# 工单详情视图
class CaseDetailView(LoginRequiredMixin, View):
    def get(self, request, case_pk):
        # 获取单个工单，id
        case = get_object_or_404(Case, pk=case_pk)

        # case detail
        pk = case_pk
        num = case.num
        status = case.status
        register = case.register
        case_context = case.context
        petitioner_name = case.petitioner.name
        petitioner_email = case.petitioner.email
        petitioner_phone = case.petitioner.phone
        petitioner_depart = case.petitioner.department.name
        petitioner_company = case.petitioner.company.name
        project = case.server.project.name
        project_num = case.server.project.project_num
        server_name = case.server.name
        server_sn = case.server.sn
        server_manufacturer = case.server.manufacturer

        context = {
            'pk': pk,
            'num': num,
            'status': status,
            'register': register,
            'case_context': case_context,
            'petitioner_name': petitioner_name,
            'petitioner_email': petitioner_email,
            'petitioner_phone': petitioner_phone,
            'petitioner_depart': petitioner_depart,
            'petitioner_company': petitioner_company,
            'project': project,
            'project_num': project_num,
            'server_name': server_name,
            'server_sn': server_sn,
            'server_manufacturer': server_manufacturer
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
        print(request.POST)
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
        context = {
            'projects': projects
        }
        return render(request, 'project.html', context)


# 项目详细视图
class ProjectDetailView(LoginRequiredMixin, View):
    # get 显示项目详情
    def get(self, request, project_pk):
        # id 获取单个项目详情
        projects = get_object_or_404(Project, pk=project_pk)

        # 获取客户公司
        companys = Company.objects.all()

        context = {
            'project': projects,
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
