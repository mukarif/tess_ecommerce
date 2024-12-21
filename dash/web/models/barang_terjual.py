from django.db import models

from .penjualan import Penjualan
from .toko import Toko


class PenjualanProduk(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    penjualan = models.ForeignKey(
        Penjualan, on_delete=models.CASCADE, null=True, blank=True)
    toko = models.ForeignKey(
        Toko, on_delete=models.CASCADE, blank=True, null=True)
    jumlah = models.IntegerField(default=0)
    harga_satuan = models.IntegerField(default=0)
    total_harga = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        nama_produk = self.toko.produk.nama
        jumlah = self.jumlah

        return '{} {}'.format(nama_produk, jumlah)

    class Meta:
        db_table = "penjualan_produk"
        verbose_name = "Penjualan Produk"
