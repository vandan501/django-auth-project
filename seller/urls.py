# In your urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='seller_dashboard'),
    path('change_password/', views.change_password, name='seller_change_password'),
]
