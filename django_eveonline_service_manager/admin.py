from django.contrib import admin
from .models import *

admin.site.register(EvePayment)
admin.site.register(EveInvoice)
admin.site.register(EveServiceTemplate)
admin.site.register(EveService)
