from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Case


# 工单视图
class CaseView(View):
    def get(self, request):
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
        }

        return render(request, 'case_detail.html', context)
