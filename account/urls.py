# account/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/login/', views.login, name='login'),
    path('account/register/', views.register, name='register'),
    path('account/activate_account/<str:uidb64>/<str:token>/', views.activate_account, name='activate_account'),
    path('account/reset_password/', views.reset_password, name='reset_password'),
    path('account/reset_password_confirm/<str:uidb64>/<str:token>/',
         views.reset_password_confirm, name='password_reset_confirm'),
]
