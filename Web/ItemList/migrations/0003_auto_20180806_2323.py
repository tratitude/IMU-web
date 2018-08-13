# Generated by Django 2.0.5 on 2018-08-06 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ItemList', '0002_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.CharField(default='', max_length=100),
        ),
    ]