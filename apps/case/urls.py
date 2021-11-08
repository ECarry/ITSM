from django.urls import path
from .views import *


urlpatterns = [
    # http://127.0.0.1:8000/case
    path('', CaseView.as_view(), name="案例管理"),
    # http://127.0.0.1:8000/case/1
    path('<int:case_pk>', CaseDetailView.as_view(), name="device_detail"),

]
