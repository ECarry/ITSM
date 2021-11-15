from django.shortcuts import render
from django.views.generic import View
from .models import *
from apps.user.mixin import LoginRequiredMixin


# 采购订单列表视图
class OrderView(LoginRequiredMixin, View):
    def get(self, request):

        orders = Order.objects.all()

        context = {
            'orders': orders,
        }

        return render(request, 'order.html', context)


# 采购订单详情
class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_pk):
        # 根据 ID 获取单个订单详情
        pass

    def post(self, request):
        # 接收 form 表单数据

        # 更新订单详情
        pass
