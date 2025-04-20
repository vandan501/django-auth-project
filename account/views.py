from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from django.urls import reverse

from account.forms import RegisterForm
from account.models import User
from account.utils import send_activation_email


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse("activate_account", kwargs={"uidb64": uidb64, "token": token})
            complete_activation_url = f"{settings.BASE_URL}{activation_link}"

            send_activation_email(user.email, complete_activation_url)

            messages.success(
                request,
                "Registration successful! Please check your email to activate your account."
            )
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {"form": form})


def login(request):
    return render(request, 'account/login.html')


def home(request):
    return render(request, 'account/home.html')


def reset_password(request):
    return render(request, 'account/reset_password.html')


def reset_password_confirm(request, uidb64, token):
    return render(request, 'account/reset_password_confirm.html')


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request, "Your account is already activated.")
            return redirect("login")

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account has been activated.")
            return redirect("login")
        else:
            messages.error(request, "Activation link is invalid or has expired.")
            return redirect("login")

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Invalid activation link. Please try again.")
        return redirect("login")
