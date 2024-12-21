from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from web.models.keranjang import Keranjang


@login_required("", "", "login")
def get_keranjang(request):
    context = {}
    data_set = Keranjang.objects
    data_set = data_set.filter(user=request.user).order_by('-created')

    array_data = []
    total_bayar = 0
    for data in data_set:
        total = data.jumlah*data.toko.harga_satuan
        array_data.append({
            "id": data.id,
            "produk": data.toko.produk.nama,
            "produk_deskripsi": data.toko.produk.deskripsi,
            "image": data.toko.foto_thum.url,
            "harga": data.toko.harga_satuan,
            "jumlah": data.jumlah,
            "total_harga": total,
        })
        total_bayar += total
    print(total_bayar)
    context['dataset'] = array_data
    context['bayar'] = total_bayar
    return render(request, 'pages_pembeli/cart.html', context=context)


@login_required("", "", "login")
def keranjang_insert(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        data = Keranjang()

        data.user = request.user
        data.toko_id = request.POST.get('id_toko')
        data.jumlah = request.POST.get('jumlah')

        data.save()

        messages.success(request, "Sukses insert data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def keranjang_update(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    if request.method == "POST":
        data = Keranjang.objects.filter(id=id).first()

        data.jumlah = request.POST.get('jumlah')
        data.save()

        messages.success(request, "Sukses update data")
        return redirect(reverer)
    messages.error(request, "Hanya method POST")
    return redirect(reverer)


@login_required("", "", "login")
def keranjang_delete(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()
    Keranjang.objects.filter(id=id).delete()

    messages.success(request, "Sukses update data")
    return redirect(reverer)


@login_required("", "", "login")
def ajax_count_keranjang(request):

    count = Keranjang.objects.filter(user=request.user).count()
    return JsonResponse({'data': count})
