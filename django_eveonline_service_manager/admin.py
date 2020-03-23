from django.contrib import admin
from .models import EvePayment, EveInvoice, EveServiceTemplate, EveService
from django.utils import timezone

admin.site.register(EvePayment)
admin.site.register(EveServiceTemplate)


@admin.register(EveInvoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'paid')

@admin.register(EveService)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'expires', 'paid')

    def paid(self, obj):
        expires_in = obj.expires - timezone.now()
        days = expires_in.days 
        if days < 5:
            return False 
        return True  
        
    paid.boolean = True