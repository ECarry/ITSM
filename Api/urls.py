from django.urls import path
from .views import order_list, device_used_count, device_list

urlpatterns = [
    path('order/', order_list, name='case_list'),
    path('device/', device_list, name='device_list'),
    path('device_used_count', device_used_count, name='device_used_count')
]
