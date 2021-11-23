from django.shortcuts import render
from django.views.generic import View
from apps.user.mixin import LoginRequiredMixin
from case.models import Case
import random


# 登录装饰器，用户没有登录，则跳转到登录页面
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # 今天未处理工单个数
        case_today = Case.objects.all().filter(status='3').count()

        context = {
            'case_today': case_today,
        }

        return render(request, 'dashboard.html', context)
