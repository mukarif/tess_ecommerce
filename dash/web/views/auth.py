import json

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from web.models.profile import Profile


def login_user(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, 'auth/login.html', context)


def auth_user(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()

    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or password is None:
        messages.info(request, 'cek Kembali Username or Password')
        return redirect('login')
    if '@' in username:
        check_user = User.objects.get(email=username)
    else:
        check_user = User.objects.get(username=username)

    if check_user:
        user = authenticate(
            request, username=check_user.username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Password is incorrect')
            return redirect('login')
    else:
        messages.info(request, 'Username is incorrect')
        return redirect('login')


def register_user(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, 'auth/register.html', context)


def register_insert(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()

    user = User.objects.create_user(
        first_name=request.POST.get('first_name'),
        last_name=request.POST.get('last_name'),
        username=request.POST.get('username'),
        email=request.POST.get('email'),
    )

    user.set_password(request.POST.get('password'))
    user.save()
    if user:

        profile = Profile()

        profile.user = user
        if request.POST.get('is_admin') == "1":
            profile.is_admin = True
        profile.save()

        return redirect(reverer)
    else:
        messages.error(request, 'Data kosong')
        return redirect(reverer)


@login_required("", "", "login")
def logout_user(request):
    logout(request)
    return redirect('login')
