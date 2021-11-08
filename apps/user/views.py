from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout


# login view http://127.0.0.1:8000/user/login
class LoginView(View):
    def get(self, request):
        # 判断是否记住用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''

        # 显示登录页面
        return render(request, 'pages-login.html', {'username': username, 'checked': checked})

    def post(self, request):
        # 进行登录处理
        # 接受数据
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        remember = request.POST.get('remember')

        # 校验数据
        if not all([username, passwd]):
            return render(request, 'pages-login.html', {'errmsg': '请输入用户名和密码', 'show_code': 'show'})

        # 登录校验
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            # 验证成功
            if user.is_active:
                # 记录用户登录状态
                login(request, user)

                # 用户激活，则跳转到主页
                response = redirect('dashboard:dashboard')
                # 是否记住用户名
                if remember == 'true':
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    response.delete_cookie('username')
                return response
            else:
                return render(request, 'pages-login.html', {'errmsg': '用户未激活', 'show_code': 'show'})
        # 返回应答
        else:
            # 验证失败，
            return render(request, 'pages-login.html', {'errmsg': '用户名密码错误或用户不存在', 'show_code': 'show'})


# logout view http://127.0.0.1:8000/user/logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        # 注销后返回到登录界面
        return redirect('user:login')


# user profile view
class UserProfileView(View):
    def get(self, request):
        return render(request, 'users-profile.html',)

    def post(self, request):
        pass
