from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View

from .models import Device, DeviceSKU
from django.contrib.auth.decorators import login_required


# Create your views here.
# def device(request):
#     return render(request, 'device.html')


# 获取所有设备信息
# # http://127.0.0.1:8000/device
class DeviceSKUView(View):
    def get(self, request):
        # 获取所有备件信息
        devices = DeviceSKU.objects.all()

        context = {
            'devices': devices,
        }
        return render(request, 'device.html', context)


# 获取单个设备详情
# http://127.0.0.1:8000/device/device_id
class DeviceDetail(View):
    def get(self, request, device_pk):
        device = get_object_or_404(DeviceSKU, pk=device_pk)

        # device detail
        name = device.name
        sn = device.sn
        pn = device.pn

        context = {
            'name': name
        }
        return render(request, 'device.html', context)

