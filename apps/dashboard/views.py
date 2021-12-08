from django.shortcuts import render
from django.views.generic import View
from apps.user.mixin import LoginRequiredMixin
from case.models import Case


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # 未处理工单个数
        case_today = Case.objects.all().filter(status='3').count()

        context = {
            'case_today': case_today,
        }

        return render(request, 'dashboard.html', context)
