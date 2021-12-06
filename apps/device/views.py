from django.db.models import Q
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View, ListView, DetailView
from apps.user.mixin import LoginRequiredMixin
from .models import Device, DeviceSKU
from django.core.paginator import Paginator


# 备件型号列表
class DeviceSKUListView(LoginRequiredMixin, ListView):
    model = DeviceSKU
    template_name = 'device_list.html'
    context_object_name = 'devices'
    search_value = ""
    order_filed = "-id"

    def get_queryset(self):
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('orderby')
        # 排序
        if order_by:
            all_devices = DeviceSKU.objects.all().order_by(order_by)
            self.order_filed = order_by
        else:
            all_devices = DeviceSKU.objects.all().order_by(self.order_filed)
        # 搜索
        if search:
            all_devices = DeviceSKU.objects.filter(Q(pn__icontains=search) | Q(spec__icontains=search))
            self.search_value = search

        self.count_total = all_devices.count()
        paginator = Paginator(all_devices, 10)
        page = self.request.GET.get('page', 1)
        devices = paginator.get_page(page)
        return devices

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceSKUListView, self).get_context_data(*args, **kwargs)
        context['count_total'] = self.count_total
        context['search'] = self.search_value
        context['orderby'] = self.order_filed
        context['objects'] = self.get_queryset()
        return context


# 备件详情
class DeviceDetailView(LoginRequiredMixin, DetailView):
    pass

