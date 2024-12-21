import json

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from web.models import Toko


def index(request):
    context = {}
    toko = Toko.objects
    search = request.POST.get('search')
    if search:
        toko = toko.filter(Q(produk__nama__icontains=search) | Q(
            produk__deskripsi__icontains=search))
    data_set = toko.filter(~Q(stok=0)).order_by('harga_satuan')

    paginator = Paginator(data_set, 12)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['dataset'] = page_obj
    return render(request, 'pages_pembeli/home.html', context)


@login_required("", "", "login")
def index_admin(request):
    context = {}
    return render(request, 'pages_penjual/home.html', context)
