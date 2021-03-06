# Generated by Django 2.2.4 on 2019-12-29 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EvePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('code', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='EveServiceTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('monthly_price', models.FloatField()),
                ('quarterly_price', models.FloatField()),
                ('annual_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EveService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('service_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_eveonline_service_manager.EveServiceTemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EveInvoice',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('84e49cdd-a84f-435c-b0d3-a7c656f5aa9c'), primary_key=True, serialize=False, unique=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_eveonline_service_manager.EveService')),
            ],
        ),
    ]
