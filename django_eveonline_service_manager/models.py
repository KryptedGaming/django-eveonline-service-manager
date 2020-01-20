from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import uuid
import pytz


class EvePayment(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.code


class EveInvoice(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True)
    service = models.ForeignKey("EveService", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_amount_paid(self):
        payments = EvePayment.objects.filter(code=self.id)
        total_amount_paid = 0
        for payment in payments:
            total_amount_paid += payment.amount

        return total_amount_paid

    def get_payments(self):
        return EvePayment.objects.filter(code=self.id)

    def get_month_modifier(self):
        total_amount_paid = self.get_amount_paid()
        if total_amount_paid >= self.service.service_template.annual_price:
            return 12
        elif total_amount_paid >= self.service.service_template.quarterly_price:
            return 3
        elif total_amount_paid >= self.service.service_template.monthly_price:
            return 1
        else:
            return None

    def process(self):
        if self.get_month_modifier():
            service = self.service
            service.expires = service.expires + \
                timedelta(days=self.get_month_modifier()*30)
            service.save()
            self.delete()


class EveServiceTemplate(models.Model):
    name = models.CharField(max_length=64)
    monthly_price = models.FloatField()
    quarterly_price = models.FloatField()
    annual_price = models.FloatField()

    def __str__(self):
        return self.name


class EveService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField(null=True, blank=True)
    service_template = models.ForeignKey(
        "EveServiceTemplate", on_delete=models.CASCADE)

    def __str__(self):
        return "<%s:%s>" % (self.service_template.name, self.user.username)

    def is_expired(self):
        return self.expires <= datetime.utcnow().replace(tzinfo=pytz.UTC)

    def is_pending_payment(self):
        return EveInvoice.objects.filter(service=self).exists()
