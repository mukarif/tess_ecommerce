from datetime import timedelta

from django.utils.timezone import now
from web.models import Penjualan


def update_status_penjualan():
    time_threshold = now() - timedelta(hours=24)
    records_to_update = Penjualan.objects.filter(created__lte=time_threshold)

    for record in records_to_update:
        record.status = -1
        record.save()
