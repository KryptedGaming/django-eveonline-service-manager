# Generated by Django 2.2.8 on 2020-01-20 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_service_manager', '0002_auto_20200120_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='eveinvoice',
            name='pending',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='eveinvoice',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8ca4488e-2bb8-4be3-bc9e-5ba7dccd56a8'), primary_key=True, serialize=False, unique=True),
        ),
    ]
