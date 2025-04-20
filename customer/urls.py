# In your urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change_password/', views.change_password, name='change_password')        
]
