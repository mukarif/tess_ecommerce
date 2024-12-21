import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from web.helpers.thumbnail import create_thumbnail
from web.models import Produk, Toko


@login_required("", "", "login")
def index(request):
    context = {}
    produk = Produk.objects.all().order_by('nama')
    data_set = Toko.objects
    search = request.GET.get('search')
    if search:
        data_set = data_set.filter(Q(user__profile_user__nama_toko__icontains=search) | Q(
            produk__nama__icontains=search))

    data_set = data_set.order_by('created')

    paginator = Paginator(data_set, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['dataset'] = page_obj
    context['produk'] = produk

    return render(request, 'pages_penjual/toko/index.html', context)


@login_required("", "", "login")
def insert_toko(request):

    reverer = request.META.get('HTTP_REFERER', '').lower()

    file = request.FILES['file']
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    extension = os.path.splitext(file.name)[1].lower()
    if extension not in valid_extensions:
        messages.error(request, "File harus image")
        return redirect(reverer)
    produk_id = request.POST.get('produk')
    toko = Toko.objects.filter(produk__id=produk_id, user=request.user).first()

    if toko:
        toko.stok = int(request.POST.get('stok')) + toko.stok
        toko.satuan = request.POST.get('satuan')
        toko.harga_satuan = request.POST.get('harga')
        toko.save()
    else:
        thumbnail = create_thumbnail(file)

        toko = Toko()

        toko.user = request.user
        toko.produk_id = produk_id
        toko.foto = file
        toko.foto_thum = thumbnail
        toko.satuan = request.POST.get('satuan')
        toko.harga_satuan = request.POST.get('harga')
        toko.stok = request.POST.get('stok')

        toko.save()

    messages.success(request, "Sukses insert data")
    return redirect(reverer)


@login_required("", "", "login")
def update_toko(request, id):

    reverer = request.META.get('HTTP_REFERER', '').lower()

    toko = Toko.objects.filter(id=id).first()

    if toko:
        if request.POST.get('edit_file'):
            file = request.FILES['edit_file']
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
            extension = os.path.splitext(file.name)[1].lower()
            if extension not in valid_extensions:
                messages.error(request, "File harus image")
                return redirect(reverer)
            thumbnail = create_thumbnail(file)
            toko.foto = file
            toko.foto_thum = thumbnail

        toko.satuan = request.POST.get('edit_satuan')
        toko.harga_satuan = request.POST.get('edit_harga')
        toko.stok = request.POST.get('edit_stok')

        toko.save()

    messages.success(request, "Sukses update data")
    return redirect(reverer)
