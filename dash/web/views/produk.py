import os

import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from web.models.produk import Produk


@login_required("", "", "login")
def get_produk(request):
    context = {}
    search = request.GET.get('search')
    data_set = Produk.objects

    if search:
        data_set = data_set.filter(Q(nama__icontains=search) | Q(
            deskripsi__icontains=search))

    data_set = data_set.order_by('nama')

    paginator = Paginator(data_set, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['dataset'] = page_obj
    return render(request, 'pages_penjual/produk/index.html', context=context)


@login_required("", "", "login")
def produk_insert_by_csv(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        valid_extensions = ['.xls', '.xlsx']
        extension = os.path.splitext(file.name)[1].lower()
        if extension not in valid_extensions:
            messages.error(request, "File harus escel")
            return redirect(reverer)
        df = pd.read_excel(file)

        # Example: Iterate through rows and save data to the database
        for _, row in df.iterrows():
            Produk.objects.create(
                nama=row['nama'],
                deskripsi=row['deskripsi']
            )
        messages.success(request, "Sukses insert data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def produk_insert(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        produk = Produk.objects.filter(nama=request.POST.get('nama')).first()
        if produk:
            produk.deskripsi = request.POST.get('deskripsi')
            produk.save()
        else:
            produk = Produk()

            produk.nama = request.POST.get('nama')
            produk.deskripsi = request.POST.get('deskripsi')
            produk.save()

        messages.success(request, "Sukses insert data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def produk_update(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        produk = Produk.objects.filter(id=id).first()

        produk.nama = request.POST.get('edit_nama')
        produk.deskripsi = request.POST.get('edit_deskripsi')
        produk.save()

        messages.success(request, "Sukses update data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)
