from django.shortcuts import render, redirect
from .models import EveService, EveServiceTemplate, EveInvoice, EvePayment


def list_services(request):
    context = {}
    context['service_templates'] = EveServiceTemplate.objects.all()
    context['services'] = EveService.objects.filter(user=request.user)
    return render(request, 'django_eveonline_service_manager/list_services.html', context=context)


def request_service(request, service_template_id):
    service_template = EveServiceTemplate.objects.get(pk=service_template_id)
    EveService.objects.create(
        user=request.user,
        service_template=service_template,
        expires=None
    )
    return redirect('django-eveonline-service-manager-service-list')


def list_invoices(request):
    context = {}
    context['invoices'] = EveInvoice.objects.filter(service__user=request.user).order_by('-paid')
    return render(request, 'django_eveonline_service_manager/list_invoices.html', context=context)


def refresh_invoice(request):
    pass
