"""dash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from web.views import (auth, bayar, home, keranjang, penjualan, produk,
                       profile, toko, user)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth.login_user, name='login'),
    path('auth/', auth.auth_user, name='auth'),
    path('register/', auth.register_user, name='register'),
    path('register/insert', auth.register_insert, name='register_insert'),
    path('logout', auth.logout_user, name='logout'),

    path('', home.index, name='home'),

    path('user/update', profile.update_user, name='update_user'),

    # ADMIN
    path('toko/home/', home.index_admin, name='home_admin'),
    path('toko/user/', user.get_user, name='users'),

    path('toko/produk/', produk.get_produk, name='produk'),
    path('toko/produk/insert', produk.produk_insert, name='produk_insert'),
    path('toko/produk/upload', produk.produk_insert_by_csv,
         name='produk_insert_csv'),
    path('toko/produk/update/<id>', produk.produk_update, name='produk_update'),


    path('toko/toko/', toko.index, name='toko'),
    path('toko/toko/insert', toko.insert_toko, name='toko_insert'),
    path('toko/toko/update/<id>', toko.update_toko, name='toko_update'),


    path('toko/laporan', penjualan.get_laporan_penjualan, name='laporan_penjulan'),

    # NON ADMIN
    path('keranjang/', keranjang.get_keranjang, name='keranjang'),
    path('keranjang/insert', keranjang.keranjang_insert, name='keranjang_insert'),
    path('keranjang/update/<id>', keranjang.keranjang_update,
         name='keranjang_update'),
    path('keranjang/delete/<id>', keranjang.keranjang_delete,
         name='keranjang_delete'),
    path('keranjang/count', keranjang.ajax_count_keranjang,
         name='keranjang_count'),

    path('history/', penjualan.get_penjualan, name='history'),
    path('penjualan/insert', penjualan.penjualan_insert, name='penjualan_insert'),
    path('penjualan/insert/satuan', penjualan.penjualan_insert_satuan,
         name='penjualan_insert_satuan'),
    path('penjualan/status/<id>', penjualan.penjualan_update_status,
         name='penjualan_update_status'),
    path('penjualan/upload/<id>', penjualan.penjualan_upload_bukti_bayar,
         name='penjualan_upload_bukti_bayar'),
    path('penjualan/detail/<id>', penjualan.list_penjualan_produk,
         name='list_penjualan_produk'),

    path('upload_bb/<id>', bayar.get_bayar, name='upload_bb'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
