from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(DeviceView.as_view()), name="所有备件"),
    # path('test/', views.device_type_list),
    # http://127.0.0.1:8000/device/1
    # path('<int:device_pk>', views.device_detail, name="device_detail"),
]
