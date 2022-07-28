from celery import shared_task
from .models import New


@shared_task
def complete_order(oid):
    news = New.objects.get(pk=oid)
    New.complete = True
    New.save()
