from django.urls import path
from .views import *

app_name = 'cart'
urlpatterns = [
    # 采购订单主页 http://127.0.0.1:8000/order
    path('', OrderView.as_view(), name="采购订单列表"),
    # 采购订单详情页 http://127.0.0.1:8000/order/pk
    path('<int:case_pk>', OrderDetailView.as_view(), name="采购订单详情"),
    # 新建采购订单页 http://127.0.0.1:8000/order/new_order
    path('new_order', NewOrderView.as_view(), name="新建订单"),
]
