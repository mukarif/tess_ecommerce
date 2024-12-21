from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from web.models import (Keranjang, Notif, Penjualan, PenjualanProduk, Profile,
                        Toko)


@login_required("", "", "login")
def get_bayar(request, id):
    context = {}
    data_set = Penjualan.objects.filter(id=id).first()
    context['data'] = data_set
    return render(request, 'pages_pembeli/bayar.html', context=context)
