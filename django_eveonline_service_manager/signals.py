from django.contrib.auth.models import User, Group
from .models import EveService, EveInvoice, EvePayment
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction
from .email import send_service_request_notification, send_service_update_notification, send_invoice_notification

import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=EveService)
def eve_service_signal(sender, **kwargs):
    def call():
        eve_service = kwargs.get('instance')
        if kwargs.get('created'):
            for user in User.objects.filter(is_superuser=True):
                send_service_request_notification(user.email, eve_service)
        else:
            send_service_update_notification(eve_service.user.email, eve_service)
    transaction.on_commit(call)

@receiver(post_save, sender=EveInvoice)
def eve_invoice_signal(sender, **kwargs):
    def call():
        eve_invoice = kwargs.get('instance')
        if kwargs.get('created'):
            send_invoice_notification(eve_invoice)
    transaction.on_commit(call)