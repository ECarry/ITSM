import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from apps.user.mixin import LoginRequiredMixin
from datetime import datetime
from device.models import Device, DeviceSKU
from case.models import Project
from django.core.paginator import Paginator


# 采购订单列表视图
class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.all()

        # 分页显示
        paginator = Paginator(orders, 10)     # 每页10个
        page_num = request.GET.get('page', 1)  # 获取分页码
        page_of_orders = paginator.get_page(page_num)

        context = {
            'orders': page_of_orders
        }

        return render(request, 'order.html', context)


# 采购订单详情
class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_pk):
        # 根据 ID 获取单个订单详情
        order = get_object_or_404(Order, pk=order_pk)

        context = {
            'order': order
        }

        return render(request, 'order_detail.html', context)

    def post(self, request):
        # 接收 form 表单数据

        # 更新订单详情
        pass


# 新建订单
class NewOrderView(LoginRequiredMixin, View):
    def get(self, request):
        # 显示备件类型
        types = Device.objects.all()
        # 备件规格
        specs = DeviceSKU.objects.all()
        # 项目
        projects = Project.objects.all()
        # 收货地址
        address = Address.objects.all()
        # 响应新建订单页面
        context = {
            'types': types,
            'specs': specs,
            'projects': projects,
            'address': address,
        }
        return render(request, 'new_order.html', context)
        pass

    def post(self, request):
        # 订单编号自动生成
        order_num = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randrange(1000, 9999))

