from django.urls import path
from .views import *

app_name = 'order'
urlpatterns = [
    # 采购订单主页 http://127.0.0.1:8000/order
    path('', OrderView.as_view(), name="order_list"),
    # 采购订单详情页 http://127.0.0.1:8000/order/pk
    path('detail/<int:order_pk>', OrderDetailView.as_view(), name="order_detail"),
    # 新建采购订单页 http://127.0.0.1:8000/order/new_order
    path('new_order', NewOrderView.as_view(), name="新建订单"),
]
