# Generated by Django 2.0.5 on 2018-11-07 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0003_auto_20181107_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='customaccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]