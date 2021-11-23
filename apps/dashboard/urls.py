from django.urls import path
from .views import DashboardView

app_name = 'dashboard'
urlpatterns = [
    path('', DashboardView.as_view(), name='控制面板'),
]
