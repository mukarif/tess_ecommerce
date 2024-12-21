import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from web.models.profile import Profile


@login_required("", "", "login")
def get_user(request):
    data_set = Profile.objects
    search = request.GET.get('search')
    if search:
        data_set = data_set.filter(Q(user__username__icontains=search) | Q(
            user__first_name__icontains=search) | Q(user__last_name__icontains=search))

    data_set = data_set.filter(
        user__is_superuser=False).order_by('-user__date_joined')

    print(data_set)
    paginator = Paginator(data_set, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "dataset": page_obj,
    }
    return render(request, 'pages_penjual/user/index.html', context=context)


@login_required("", "", "login")
def create_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    # password = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']
    jabatan = int(request.POST['jabatan'])
    birthdate = request.POST['tanggal_lahir']
    gender = request.POST['gender']
    is_admin = request.POST['is_admin']
    # return HttpResponse(str(email))

    count = User.objects.filter(username=username).count()

    if count > 0:

        messages.error(request, 'Username Sudah digunakan')
        return redirect(reverse('tambah_user'))

    count_email = User.objects.filter(email=email).count()

    if count_email > 0:

        messages.error(request, 'Email Sudah digunakan')
        return redirect(reverse('tambah_user'))

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
    )
    # user.set_password(password)
    user.set_password(os.getenv('PASSWORD_DEFAULT_USER'))
    user.save()

    # profile = Profile.objects.filter(user=user).first()
    profile = Profile()
    profile.user = user
    profile.nrp = username
    profile.gender = gender
    profile.birthdate = birthdate
    # profile.jabatan = jabatan
    profile.phone = phone
    if is_admin == "1":
        profile.is_admin = True
    else:
        profile.is_admin = False
    profile.save()

    return redirect(reverse("user"))


@login_required("", "", "login")
def edit_user(request, id):
    context = {}
    users = User.objects.filter(id=id).first()

    context['data'] = users
    return render(request, 'web_v2/pages/users/edit.html', context)


@login_required("", "", "login")
def update_user(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    email = request.POST['email']
    phone = request.POST['phone']
    jabatan = int(request.POST['jabatan'])
    birthdate = request.POST['tanggal_lahir']
    gender = request.POST['gender']
    is_admin = request.POST['is_admin']
    # return HttpResponse(str(email))
    user = User.objects.get(id=id)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    if password != "":
        user.set_password(password)

    user.save()

    return redirect(reverse("user"))


@login_required("", "", "login")
def delete_user(request, id):
    obj = User.objects.get(id=id)
    obj.delete()
    return redirect(reverse('user'))
    # return render(request,'web/pages/users/index.html')
