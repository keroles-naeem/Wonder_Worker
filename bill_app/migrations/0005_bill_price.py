# Generated by Django 5.1 on 2024-09-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0004_remove_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]