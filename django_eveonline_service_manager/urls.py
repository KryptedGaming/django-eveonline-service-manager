from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.list_services,
         name='django-eveonline-service-manager-service-list'),
    path('<int:service_template_id>/request/',
         views.request_service,
         name='django-eveonline-service-manager-service-request'),
    path('invoices/',
         views.list_invoices,
         name='django-eveonline-service-manager-invoice-list'),
    path('invoices/<int:invoice_id>/payments/refresh/',
         views.refresh_invoice,
         name='django-eveonline-service-manager-invoice-refresh'),
]
