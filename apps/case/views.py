from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import View
from .models import *


# 工单视图
class CaseView(View):
    def get(self, request):
        # 获取所有工单

        cases = Case.objects.all()

        context = {'cases': Case.objects.all()}
        return render(request, 'case.html', context)


# 工单详情视图
class CaseDetailView(View):
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
class NewProjectView(View):
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
        # 获取用户输入信息
        project_name = request.POST.get('project_name')
        project_num = request.POST.get('project_num')
        contract_num = request.POST.get('contract_num')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        company = request.POST.get('company_id')

        # 判断数据是否完整
        if not all([project_name, project_num, contract_num, start_time, end_time, company]):
            return render(request, 'project.html', {'errmsg': "数据不完整"})

        # 判断是否已存在项目
        try:
            p = Project.objects.get(project_num=project_num)
        except Project.DoesNotExist:
            # 项目不存在
            p = None

        if p:
            return render(request, 'new_project.html', {'errmsg': "项目编号" + " " + project_num + " " + "已存在", 'error_show': "show"})

        # 保存数据
        Project.objects.create(name=project_name,
                               project_num=project_num,
                               contract_num=contract_num,
                               start_time=start_time,
                               end_time=end_time,
                               company_id=company)

        return render(request, 'new_project.html', {'msg': "项目创建成功", 'success_show': "show"})


# 项目视图
class ProjectView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request, 'project.html', context)


# 项目详细视图
class ProjectDetailView(View):
    # get 显示项目详情
    def get(self, request, project_pk):
        # id 获取单个项目详情
        project = get_object_or_404(Project, pk=project_pk)

        # project detail
        project_name = project.name
        project_num = project.project_num
        contract_num = project.contract_num
        create_time = project.create_time
        start_time = project.start_time
        end_time = project.end_time
        company = project.company.name

        context = {
            'project_name': project_name,
            'project_num': project_num,
            'contract_num': contract_num,
            'create_time': create_time,
            'start_time': start_time,
            'end_time': end_time,
            'company': company
        }

        return render(request, 'project_detail.html', context)

    # post 更新项目
    def post(self, request):
        # 获取输入信息
        project_name = request.POST.get('project_name')
        project_num = request.POST.get('project_num')
        contract_num = request.POST.get('contract_num')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        company = request.POST.get('company')


