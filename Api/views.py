import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import OrderSerializer, DeviceSerializer
from cart.models import Order
from device.models import Device


@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def device_list(request):
    if request.method == 'GET':
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def device_used_count(request):
    now_time = datetime.datetime.now()
    if request.method == 'GET':
        # disk_count = Device.objects.filter(status=2).filter(last_time__month=now_time.month).count()
        disk_count = Device.objects.filter(sku__spu__name='硬盘').count()
        print(disk_count)
        return JsonResponse(disk_count, safe=False)
