# Generated by Django 3.1 on 2024-10-15 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='order_product',
            name='size',
        ),
    ]
