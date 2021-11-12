from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'cart'
urlpatterns = [
    # 采购订单主页 http://127.0.0.1:8000/order
    path('', login_required(OrderView.as_view()), name="采购订单列表"),
    # 采购订单详情页 http://127.0.0.1:8000/order/pk
    path('<int:case_pk>', login_required(OrderDetailView.as_view()), name="采购订单详情"),
]
