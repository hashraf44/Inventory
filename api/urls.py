from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WebsiteViewSet, CustomerViewSet, ShippingAddressViewSet, OrderViewSet, StockTransferViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'websites', WebsiteViewSet, basename='website')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'addresses', ShippingAddressViewSet, basename='address')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'stock-transfers', StockTransferViewSet, basename='stock-transfer')

urlpatterns = [
    path('v1/', include(router.urls)),
]
