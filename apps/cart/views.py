import random
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import View
from .models import *
from apps.user.mixin import LoginRequiredMixin
from datetime import datetime
from device.models import Device, DeviceSKU
from case.models import Project, Case
from django.core.paginator import Paginator
from django.contrib import messages
from utils.track import KuaiDi100
import json


# 采购订单列表视图
class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.all()
        # 分页显示
        paginator = Paginator(orders, 10)  # 每页10个
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

        # 获取该订单物流公司和订单编号
        track_num = order.track_num
        track_id = order.track_id
        try:
            track_company = get_object_or_404(TrackCompany, pk=track_id).code
        except:
            track_company = ''

        # 物流公司
        tracks = TrackCompany.objects.all()

        # 获取物流信息返回 json
        result = json.loads(KuaiDi100().track(track_company, track_num, '', '', ''))
        print(result)

        # 物流状态
        try:
            track_status = int(result['state'])
        except:
            track_status = 1

        # 物流信息列表
        try:
            track_list = result['data']
        except:
            track_list = None

        # 颜色
        color = ('text-warning', 'text-success', 'text-danger', 'text-info', 'text-muted')

        context = {
            'order': order,
            'tracks': tracks,
            'track_status': track_status,
            'track_list': track_list,
            'color': color
        }

        return render(request, 'order_detail.html', context)

    def post(self, request, order_pk):
        # case
        case_num = request.POST.get('case_num')
        # try:
        #     c = Case.objects.filter(num=case_num)
        # except Case.DoesNotExist:
        #     c = None

        # 工单不存在，报错，返回
        # if not c:
        #     messages.error(request, '工单不存在')
        #     return redirect('order:order_list')
        # case = Case.objects.get(num=case_num)
        # case_id = case.id

        # 接收 form 表单数据
        info = request.POST.dict()
        del info['csrfmiddlewaretoken']
        # del info['case_num']
        # info['case_id'] = case_id
        # 获取订单 ID
        order = Order.objects.filter(id=order_pk)
        # 更新订单详情
        order.update(**info)
        messages.success(request, '修改成功')
        return redirect('order:order_list')


# 新建订单
class NewOrderView(LoginRequiredMixin, View):
    def get(self, request):
        # 备件数量
        order = Order.objects.all()
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
            'order': order,
        }
        return render(request, 'new_order.html', context)
        pass

    def post(self, request):
        # 订单编号自动生成
        order_num = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randrange(1000, 9999))
        # 获取当前用户 ID
        current_user_id = request.user.id
        post = request.POST.dict()
        del post['csrfmiddlewaretoken']
        post['order_num'] = order_num
        post['order_name_id'] = current_user_id
        print(post)
        # 保存数据
        Order.objects.create(**post)
        return redirect('order:order_list')
