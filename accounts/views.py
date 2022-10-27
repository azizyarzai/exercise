from email import message
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()


# Create your views here.


def register_user(request):
    if request.user.is_authenticated:
        return redirect('products:list')
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    else:
        email = request.POST.get("email")
        name = request.POST.get("name")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1 != pass2:
            messages.error(request, "Password does not match.")
            return redirect('accounts:register')

        exists = User.objects.filter(email=email).exists()
        if exists:
            messages.error(request, 'Email already exist.')
            return redirect('accounts:register')

        user = User.objects.create_user(name=name, email=email, password=pass1)
        messages.success(request, 'User was created successfully.')
        return redirect("products:list")


def login_user(request):
    if request.user.is_authenticated:
        return redirect('products:list')
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    else:
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")

        user = authenticate(request, email=email, password=pass1)
        if not user:
            messages.error(request, 'Wrong credentials.')
            return redirect("accounts:login")

        login(request, user)
        messages.success(request, 'You are logged in successfully.')
        return redirect("products:list")


@login_required
def logout_user(request):
    logout(request)
    return redirect("products:list")
