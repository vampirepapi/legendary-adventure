# Generated by Django 4.0 on 2021-12-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='product_id',
        ),
    ]
