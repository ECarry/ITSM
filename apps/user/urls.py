from django.urls import path
from .views import LoginView, LogoutView, UserProfileView, RegisterView
from django.contrib.auth.decorators import login_required

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-profile/', login_required(UserProfileView.as_view()), name='user-profile'),
]
