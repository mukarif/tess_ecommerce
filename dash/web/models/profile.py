from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="profile_user", on_delete=models.CASCADE)
    nama_toko = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_penjual = models.BooleanField(default=False)
    is_pembeli = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):

        username = self.user.username
        phone = self.phone

        return '{} {}'.format(username, phone)

    class Meta:
        db_table = "profiles"
        verbose_name = "Profile"
