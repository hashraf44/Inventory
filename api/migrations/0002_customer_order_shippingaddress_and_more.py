# Generated by Django 4.2.4 on 2024-06-20 17:27

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['uuid', 'product', 'platform'],
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('default', models.BooleanField(default=False, help_text='To choose customer default delivery address')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
            options={
                'verbose_name': 'Shipping Address',
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
        migrations.RenameModel(
            old_name='Stock_transfer',
            new_name='StockTransfer',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Contact_details',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='stocktransfer',
            options={'ordering': ['transfer_date'], 'verbose_name': 'Stock Transfer', 'verbose_name_plural': 'Stock Transfers'},
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'ordering': ['name'], 'verbose_name': 'Website', 'verbose_name_plural': 'Websites'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock_keeping_unit',
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='DEFAULT_SKU', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.SlugField(max_length=255),
        ),
        migrations.DeleteModel(
            name='eCommerceOrder',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shippingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.website'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]
