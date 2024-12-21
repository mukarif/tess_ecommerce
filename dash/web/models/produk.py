from django.db import models


class Produk(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    nama = models.CharField(max_length=200, blank=False,
                            null=False, unique=True)
    deskripsi = models.TextField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        nama = self.nama
        return '{}'.format(nama)

    class Meta:
        db_table = 'produk'
        verbose_name_plural = 'Produk'
