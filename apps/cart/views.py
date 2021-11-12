from django.shortcuts import render
from django.views.generic import View
from .models import *


# 采购订单列表视图
class OrderView(View):
    def get(self, request):

        orders = Order.objects.all()

        context = {
            'orders': orders,
        }

        return render(request, 'order.html', context)


# 采购订单详情
class OrderDetailView(View):
    def ger(self, request, order_pk):
        # 根据 ID 获取单个订单详情
        pass

    def post(self, request):
        # 接受 form 表单

        # 更新订单详情
        pass
