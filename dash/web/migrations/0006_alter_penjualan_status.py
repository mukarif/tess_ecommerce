# Generated by Django 3.2.15 on 2024-12-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_penjualan_bukti_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penjualan',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'PROSES'), (1, 'PACKING'), (2, 'KIRIM'), (100, 'SELESAI'), (-1, 'GAGAL')], default=0),
        ),
    ]
