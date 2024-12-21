from celery import shared_task
from web.services.update_status_penjualan import update_status_penjualan


@shared_task
def add(x, y):
    return x + y


@shared_task(bind=True)
def update_gagal(self):

    update_status_penjualan()

    print("End")

    return "Done"
