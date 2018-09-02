# Generated by Django 2.0.5 on 2018-09-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(default='', max_length=20)),
                ('items', models.ManyToManyField(to='ItemList.Item')),
            ],
        ),
    ]
