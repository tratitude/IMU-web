# Generated by Django 2.0.5 on 2018-11-07 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180831_0138'),
        ('shoppingCart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='customaccount',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.user_detail'),
        ),
    ]
