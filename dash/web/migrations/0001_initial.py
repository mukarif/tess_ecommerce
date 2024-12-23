# Generated by Django 3.2.15 on 2024-12-18 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('bukti_transfer', models.FileField(blank=True, null=True, upload_to='images/produk/')),
                ('total_harga', models.IntegerField(default=0)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'PROSES'), (1, 'KIRIM'), (2, 'SELESAI'), (-1, 'GAGAL')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('user_pembeli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Penjualan',
                'db_table': 'penjualan',
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nama', models.CharField(max_length=200, unique=True)),
                ('deskripsi', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Produk',
                'db_table': 'produk',
            },
        ),
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='images/produk/')),
                ('foto_thum', models.FileField(blank=True, null=True, upload_to='images/thum/')),
                ('satuan', models.CharField(blank=True, max_length=100, null=True)),
                ('harga_satuan', models.IntegerField(default=0)),
                ('stok', models.IntegerField(default=0)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('produk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.produk')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_penjual', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Toko',
                'db_table': 'toko',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_toko', models.CharField(max_length=200)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('is_penjual', models.BooleanField(default=False)),
                ('is_pembeli', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='PenjualanProduk',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('jumlah', models.IntegerField(default=0)),
                ('harga_satuan', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('penjualan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.penjualan')),
                ('toko', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.toko')),
            ],
            options={
                'verbose_name': 'Penjualan Produk',
                'db_table': 'penjualan_produk',
            },
        ),
        migrations.CreateModel(
            name='Notif',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('judul', models.CharField(max_length=200)),
                ('pesan', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tujuan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notifikasi',
                'db_table': 'notifikasi',
            },
        ),
        migrations.CreateModel(
            name='Keranjang',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('jumlah', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('toko', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.toko')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keranjang_pembeli', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Keranjang',
                'db_table': 'keranjang',
            },
        ),
    ]
