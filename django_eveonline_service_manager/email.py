from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse 

service_request_template = """
%s has requsted the following service: %s. 
"""

service_update_template = """
Your service %s_%s has been updated. 

Expires: %s
Notes: %s

For more details visit https://%s%s
"""

invoice_creation_template = """
An invoice for your service %s_%s has been created. 

Please view it here: https://%s%s 
"""
def send_service_request_notification(email, service):
    send_mail(
        'Service Request Notification',
        service_request_template % (service.user, service.service_template.name),
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

def send_service_update_notification(email, service):
    send_mail(
        'Service Update Notification',
        service_update_template % (service.service_template.name, service.pk, service.expires.strftime("%Y-%m-%d"), service.notes, settings.SITE_DOMAIN, reverse('django-eveonline-service-manager-service-list')),
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

def send_invoice_notification(invoice):
    send_mail(
        'Invoice Notification',
        invoice_creation_template % (invoice.service.service_template.name, invoice.service.pk, settings.SITE_DOMAIN, reverse('django-eveonline-service-manager-invoice-list')),
        settings.DEFAULT_FROM_EMAIL,
        [invoice.service.user.email],
        fail_silently=False,
    )
