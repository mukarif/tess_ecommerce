from django.contrib.auth.models import User
from django.db import models

from .produk import Produk


class Toko(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    user = models.ForeignKey(
        User, related_name="user_penjual", on_delete=models.CASCADE, null=True, blank=True)
    produk = models.ForeignKey(
        Produk, on_delete=models.CASCADE, blank=True, null=True)
    foto = models.FileField(upload_to='images/produk/', blank=True, null=True)
    foto_thum = models.FileField(
        upload_to='images/thum/', blank=True, null=True)
    satuan = models.CharField(max_length=100, blank=True,
                              null=True)
    harga_satuan = models.IntegerField(default=0)
    stok = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        nama_produk = self.produk.nama
        username = self.user.username

        return '{} {}'.format(nama_produk, username)

    class Meta:
        db_table = "toko"
        verbose_name = "Toko"
