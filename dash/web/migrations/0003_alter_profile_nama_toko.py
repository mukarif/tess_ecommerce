# Generated by Django 3.2.15 on 2024-12-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nama_toko',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]