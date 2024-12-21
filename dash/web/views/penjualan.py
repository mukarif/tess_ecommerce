from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from web.models import (Keranjang, Notif, Penjualan, PenjualanProduk, Profile,
                        Toko)


@login_required("", "", "login")
def get_penjualan(request):
    context = {}
    data_set = PenjualanProduk.objects
    data_set = data_set.filter(
        penjualan__user_pembeli=request.user).order_by('-created')

    paginator = Paginator(data_set, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['dataset'] = page_obj
    return render(request, 'pages_pembeli/history.html', context=context)


@login_required("", "", "login")
def get_laporan_penjualan(request):
    context = {}
    profile = Profile.objects.filter(user=request.user).first()
    penjual_in_pp = PenjualanProduk.objects.filter(
        toko__user=request.user).values_list('penjualan')
    data_set = Penjualan.objects
    if not profile.is_admin:
        data_set = data_set.filter(id__in=penjual_in_pp, status__gt=0)
    data_set = data_set.order_by('-created')

    paginator = Paginator(data_set, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['dataset'] = page_obj
    return render(request, 'pages_penjual/laporan/penjualan.html', context=context)


@login_required("", "", "login")
def penjualan_insert(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        data = Penjualan()

        data.user_pembeli = request.user
        data.total_harga = request.POST.get('total_harga')

        data.save()

        # Collect all inputs with name="tags[]"
        list_id = request.POST.getlist('id_cart[]')
        list_total = request.POST.getlist('total_cart[]')
        index = 0
        for i in list_id:
            print(i)
            print(list_total[index])

            cart = Keranjang.objects.filter(id=i).first()
            pb = PenjualanProduk()

            pb.penjualan = data
            pb.toko = cart.toko
            pb.harga_satuan = cart.toko.harga_satuan
            pb.jumlah = cart.jumlah
            pb.total_harga = list_total[index]

            pb.save()

            toko = cart.toko

            toko.stok = toko.stok-cart.jumlah

            toko.save()

            index += 1
            cart.delete()

        profile = Profile.objects.filter(is_admin=True).first()
        notif = Notif()

        notif.penjualan = data
        notif.judul = "Pembelian masuk"
        notif.pesan = "Jumlah barang pesanan {}".format(index+1)
        notif.tujuan = profile.user

        notif.save()

        messages.success(request, "Sukses insert data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def penjualan_insert_satuan(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        id_toko = request.POST.get('id_toko_satuan')
        jumlah = request.POST.get('jumlah_satuan')
        check_toko = Toko.objects.filter(id=id_toko).first()
        if check_toko:
            total = check_toko.harga_satuan*int(jumlah)
            data = Penjualan()

            data.user_pembeli = request.user
            data.total_harga = total

            data.save()

            pb = PenjualanProduk()

            pb.penjualan = data
            pb.toko = check_toko
            pb.harga_satuan = check_toko.harga_satuan
            pb.jumlah = jumlah
            pb.total_harga = total

            pb.save()

            check_toko.stok = check_toko.stok-int(jumlah)

            check_toko.save()

        profile = Profile.objects.filter(is_admin=True).first()
        notif = Notif()

        notif.penjualan = data
        notif.judul = "Pembelian masuk"
        notif.pesan = "Jumlah barang pesanan {}".format(jumlah)
        notif.tujuan = profile.user

        notif.save()

        messages.success(request, "Sukses insert data")
        return redirect("upload_bb", data.id)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def penjualan_update_status(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        data = Penjualan.objects.filter(id=id).first()
        if request.POST.get('status'):
            data.status = request.POST.get('status')
            data.save()

        messages.success(request, "Sukses update data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def penjualan_upload_bukti_bayar(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        data = Penjualan.objects.filter(id=id).first()
        files = request.FILES['bukti_transfer']
        if files:
            data.bukti_transfer = files
            data.save()

        messages.success(request, "Sukses update data")
        return redirect("history")
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def list_penjualan_produk(request, id):
    penjualan = Penjualan.objects.filter(id=id).first()

    data_set = PenjualanProduk.objects.filter(penjualan=penjualan)

    array_data = []
    for data in data_set:
        format_currency_harga = f"RP {data.harga_satuan:,.2f}"
        format_currency_total = f"RP {data.total_harga:,.2f}"
        array_data.append({
            'produk': data.toko.produk.nama,
            'toko': data.toko.user.profile_user.nama_toko,
            'harga_satuan': format_currency_harga,
            'jumlah': data.jumlah,
            'total_harga': format_currency_total,
        })
    return JsonResponse({'data': array_data})
