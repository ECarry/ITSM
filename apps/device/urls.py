from django.urls import path
from .views import *

app_name = 'device'
urlpatterns = [
    # SPU ADD
    path('spu/add', add_spu_popup, name="add_spu"),
    # Manufacturer ADD
    path('manufacturer/add', add_manufacturer_popup, name="add_manufacturer"),
    # SKU
    path('sku/', DeviceSKUListView.as_view(), name="sku_list"),
    # path('test/', views.device_type_list),
    # http://127.0.0.1:8000/device/1
    path('sku/<int:sku_pk>', DeviceSKUDetailView.as_view(), name="sku_detail"),
    path('sku/new_sku', NewDeviceSKUView.as_view(), name="new_sku"),

    # Devices
    path('', DeviceView.as_view(), name="device_list"),
    path('new_device/<int:sku_pk>', NewDevice.as_view(), name="new_device"),
]
