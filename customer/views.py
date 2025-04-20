from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'customer/dashboard.html')

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, "Password changed successfully... please login with your new password.")
            return redirect("login")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'customer/password_change.html', {'form': form})
