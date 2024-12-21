from django.contrib.auth.models import User
from django.db import models

from .toko import Toko


class Keranjang(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, related_name="keranjang_pembeli", on_delete=models.CASCADE, null=True, blank=True)
    toko = models.ForeignKey(
        Toko, on_delete=models.CASCADE, blank=True, null=True)
    jumlah = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        nama_produk = self.toko.produk.nama
        jumlah = self.jumlah

        return '{} {}'.format(nama_produk, jumlah)

    class Meta:
        db_table = "keranjang"
        verbose_name = "Keranjang"
