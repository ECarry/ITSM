from django.urls import path
from .views import case

app_name = 'dashboard'
urlpatterns = [
    path('', case, name='dashboard'),
]
