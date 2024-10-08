# Generated by Django 5.1 on 2024-09-23 09:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=20)),
                ('customer_number', models.IntegerField(primary_key=True, serialize=False)),
                ('cus_note', models.CharField(max_length=20, null=True)),
                ('cus_acc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('protien', models.DecimalField(decimal_places=2, max_digits=5, max_length=1, null=True)),
                ('weight', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bill_app.customer')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cus_paid', models.IntegerField(default=0)),
                ('cus_id', models.ForeignKey(default=1210366070, on_delete=django.db.models.deletion.CASCADE, to='bill_app.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill_app.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
    ]
