from django.apps import AppConfig


class DjangoEveOnlineServiceManagerConfig(AppConfig):
    name = 'django_eveonline_service_manager'
    url_slug = 'services'


    def ready(self):
        from django.db.models.signals import post_save
        from .signals import eve_service_signal, eve_invoice_signal
        from .models import EveService, EveInvoice, EvePayment
        post_save.connect(eve_service_signal, sender=EveService)
        post_save.connect(eve_invoice_signal, sender=EveInvoice)