# Generated by Django 4.2.4 on 2024-06-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customer_order_shippingaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='TEMP_SKU', max_length=10, unique=True),
        ),
    ]
