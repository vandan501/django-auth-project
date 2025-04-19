from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    return render(request, 'account/register.html')

def login(request):
    return render(request, 'account/login.html')

def home(request):
    return render(request, 'account/home.html')

def reset_password(request):
    return render(request, 'account/reset_password.html')

def reset_password_confirm(request, uidb64, token):
    return render(request, 'account/reset_password_confirm.html')
