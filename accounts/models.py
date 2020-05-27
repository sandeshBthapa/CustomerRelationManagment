from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    def __str__(self):
        return f' Customer name is: {self.name}'


class Tags(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    caterories = (
        ('Indoor', 'Indoor'),
        ('OutDoor', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=caterories)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tags)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Name of the product is : {self.name}'


class Orders(models.Model):
    STATUS = (
        ('PEN', 'Pending'),
        ('OFD', 'Out For Delivery'),
        ('DIR', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=3, choices=STATUS)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'Orders'
