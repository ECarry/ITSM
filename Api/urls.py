from django.urls import path
from .views import order_list, device_used_count, device_list, count, case

urlpatterns = [
    path('order/', order_list, name='case_list'),
    path('device/', device_list, name='device_list'),
    path('device_used_count', device_used_count, name='device_used_count'),
    path('all_count', count, name='all_count'),
    path('case', case, name='case')
]
