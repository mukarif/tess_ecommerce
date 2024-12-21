from django.contrib.auth.models import User
from django.db import models

from .toko import Toko


class Penjualan(models.Model):

    PROSES = 0
    PACKING = 1
    KIRIM = 2
    SELESAI = 100
    GAGAL = -1

    STATUS = (
        (PROSES, 'PROSES'),
        (PACKING, 'PACKING'),
        (KIRIM, 'KIRIM'),
        (SELESAI, 'SELESAI'),
        (GAGAL, 'GAGAL'),
    )

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    user_pembeli = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.SmallIntegerField(
        choices=STATUS, default=PROSES)
    bukti_transfer = models.FileField(
        upload_to='images/bukti/', blank=True, null=True)
    total_harga = models.IntegerField(default=0)
    keterangan = models.TextField(
        blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        nama_produk = self.user_pembeli.username
        jumlah = self.total_harga

        return '{} {}'.format(nama_produk, jumlah)

    class Meta:
        db_table = "penjualan"
        verbose_name = "Penjualan"
