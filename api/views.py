from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Product, Website, Customer, ShippingAddress, Order, StockTransfer
from .serializers import ProductSerializer, WebsiteSerializer, CustomerSerializer, ShippingAddressSerializer, OrderSerializer, StockTransferSerializer

class ProductViewSet(viewsets.GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

class CustomerViewSet(viewsets.GenericViewSet,
                            ListModelMixin,
                            CreateModelMixin,
                            RetrieveModelMixin,
                            UpdateModelMixin,
                            DestroyModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShippingAddressViewSet(viewsets.GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class StockTransferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockTransfer.objects.all()
    serializer_class = StockTransferSerializer
