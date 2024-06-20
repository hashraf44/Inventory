from uuid import uuid4
from django.db import models
from api.managers import BaseModelManager
from phonenumber_field.modelfields import PhoneNumberField

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.SlugField(max_length= 255)
    sku= models.CharField(max_length= 10, unique=True, default='TEMP_SKU')
    description = models.TextField()
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    unit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.name} - {self.description[:30]} - {self.price}'
    

class Website(BaseModel):
    name = models.SlugField(max_length=50, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return self.name
    
    
class Customer(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)   
    mobile = PhoneNumberField(blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ShippingAddress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    default = models.BooleanField(default= False, help_text= 'To choose customer default delivery address')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f'{self.customer.first_name}, {self.postal_code}, {self.country}'
    
class Order(BaseModel):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()
    platform = models.ForeignKey(Website, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete= models.CASCADE)

    class Meta:
        ordering = ['uuid', 'product', 'platform']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'{self.uuid} - {self.product.name}'

class StockTransfer(BaseModel):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()
    transfer_date = models.DateTimeField(auto_now_add= True)
    source = models.CharField(max_length= 255)
    destination = models.CharField(max_length= 255)

    class Meta:
        ordering = ['transfer_date']
        verbose_name = "Stock Transfer"
        verbose_name_plural = "Stock Transfers"

    def __str__(self):
        return f'Transfer of {self.product.name} on {self.transfer_date}'