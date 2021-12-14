import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import OrderSerializer, DeviceSerializer
from cart.models import Order
from device.models import Device
from case.models import Case

CURRENT_TIME = datetime.datetime.now()
CURRENT_MONTH = CURRENT_TIME.month
CURRENT_YEAR = CURRENT_TIME.year
CURRENT_DAY = CURRENT_TIME.day


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
    current_month = now_time.month
    weekday_range = range(now_time.weekday())
    for w in weekday_range:
        print(w)
    print("当前月份为：" + str(current_month))
    if request.method == 'GET':
        # disk_count = Device.objects.filter(status=2).filter(last_time__month=now_time.month).count()
        disk_count = Device.objects.filter(sku__spu__name='内存').filter(status=2).filter(last_time__month=current_month).count()

        return JsonResponse(disk_count, safe=False)


@csrf_exempt
def count(request):

    current_month_case_count = Case.objects.filter(create_time__month=CURRENT_MONTH).count()
    current_month_device_used_count = Device.objects.filter(status=2).filter(last_time__month=CURRENT_MONTH).count()
    current_month_order_count = Order.objects.filter(create_time__month=CURRENT_MONTH).count()

    all_count = [
        {
            'name': 'case',
            'data': current_month_case_count
        },
        {
            'name': 'device',
            'data': current_month_device_used_count
        },
        {
            'name': 'order',
            'data': current_month_order_count
        }
    ]

    return JsonResponse(all_count, safe=False)


def case(request):
    if request.method == 'GET':
        data = []
        for i in range(1, 32):
            all_case_count = Case.objects.filter(create_time__month=CURRENT_MONTH).filter(create_time__day=i).count()
            data.append(all_case_count)
        list = {
            'name': '所有工单',
            'data': data
        }
        print(list)
        return JsonResponse(list, safe=False)
