from django.contrib.auth.models import User
from django.db import models
from web.models import Penjualan


class Notif(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    penjualan = models.ForeignKey(
        Penjualan, on_delete=models.CASCADE, null=True, blank=True)
    judul = models.CharField(max_length=200, blank=False,
                             null=False)
    pesan = models.TextField(blank=False, null=True)
    tujuan = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        judul = self.judul
        return '{}'.format(judul)

    class Meta:
        db_table = 'notifikasi'
        verbose_name_plural = 'Notifikasi'
