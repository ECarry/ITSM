from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# 登录装饰器，用户没有登录，则跳转到登录页面
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

