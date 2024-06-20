from rest_framework import serializers
from .models import Product, Website, Customer, ShippingAddress, Order, StockTransfer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("created", "updated")

class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Website
        exclude = ("created", "updated")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ("created", "updated")

class ShippingAddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShippingAddress
            exclude = ("created", "updated")

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = Order
        exclude = ("created", "updated")

class StockTransferSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = StockTransfer
        exclude = ("created", "updated")
