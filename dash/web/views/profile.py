import json

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from web.models.profile import Profile


@login_required("", "", "login")
def update_user(request):

    if request.method == "POST":
        profile = Profile.objects.filter(user=request.user).first()

        if profile:
            profile.nama_toko = request.POST.get(
                'nama_toko') if request.POST.get('nama_toko') else None
            profile.alamat = request.POST.get(
                'alamat') if request.POST.get('alamat') else None
            profile.phone = request.POST.get(
                'phone') if request.POST.get('phone') else None
            if request.POST.get('admin') != "1":
                profile.is_penjual = True
            else:
                profile.is_admin = True

            profile.save()
        else:
            profile = Profile()

            profile.user = request.user
            profile.nama_toko = request.POST.get(
                'nama_toko') if request.POST.get('nama_toko') else None
            profile.alamat = request.POST.get(
                'alamat') if request.POST.get('alamat') else None
            profile.phone = request.POST.get(
                'phone') if request.POST.get('phone') else None
            if request.POST.get('admin') != "1":
                profile.is_penjual = True
            else:
                profile.is_admin = True

            profile.save()

        messages.success(request, "Sukses update profile")

    reverer = request.META.get('HTTP_REFERER', '').lower()
    return redirect(reverer)
