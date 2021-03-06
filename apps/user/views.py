from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from .mixin import LoginRequiredMixin


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
        return render(request, 'user/pages-login.html', {'username': username, 'checked': checked})

    def post(self, request):
        # 进行登录处理
        # 接受数据
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        remember = request.POST.get('remember')

        # 校验数据
        if not all([username, passwd]):
            return render(request, 'user/pages-login.html', {'errmsg': '请输入用户名和密码', 'show_code': 'show'})

        # 登录校验
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            # 验证成功
            if user.is_active:
                # 记录用户登录状态
                login(request, user)

                # 用户激活，则跳转到主页
                response = redirect('dashboard:dashboard')  # redirect('namespace:url name')
                # 是否记住用户名

                if remember == 'true':
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie('username')
                return response
            else:
                return render(request, 'user/pages-login.html', {'errmsg': '用户未激活', 'show_code': 'show'})
        # 返回应答
        else:
            # 验证失败，
            return render(request, 'user/pages-login.html', {'errmsg': '用户名密码错误或用户不存在', 'show_code': 'show'})


# logout view http://127.0.0.1:8000/user/logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        # 注销后返回到登录界面
        return redirect('user:login')


# user profile view
class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/users-profile.html', )

    def post(self, request):
        pass


# register view http://127.0.0.1:8000/user/register
class RegisterView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        # 接收数据并校验数据
        username = request.POST.get('username')
        passwd1 = request.POST.get('passwd1')
        passwd2 = request.POST.get('passwd2')
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        active = request.POST.get('active')
        staff = request.POST.get('staff')
        su = request.POST.get('su')

        if not all([username, passwd1, passwd2, email, mobile, name]):
            # 数据不完整
            return render(request, 'user/register.html', {'errmsg': "数据不完整", 'error_show': 'show'})

        # 判断两侧密码是否一样
        if not passwd1 == passwd2:
            return render(request, 'user/register.html', {'errmsg': "两次密码不一致", 'error_show': 'show'})

        # 校验 username 是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名存在
            return render(request, 'user/register.html', {'errmsg': "用户名存在", 'error_show': 'show'})

        # 用户注册
        user = User.objects.create_user(username=username, email=email)
        user.set_password(passwd1)

        # 判断是否激活账户
        if active == 'on':
            user.is_active = 1

        # 判断用户是否有管理权限
        if staff == 'on':
            user.is_staff = 1

        # 判断用户是否为su
        if su == 'on':
            user.is_superuser = 1
        user.mobile = mobile
        user.name = name
        user.save()

        return render(request, 'user/register.html', {'msg': "账号创建成功", 'success_show': 'show'})
