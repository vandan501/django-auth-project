from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'customer/dashboard.html')


def change_password(request):
    return render(request, 'customer/password_change.html')
