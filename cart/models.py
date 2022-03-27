from __future__ import unicode_literals

from django.db import models

from account.models import Profile
from product.models import Product

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="owner", null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.pr_price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class OrderItem(models.Model):
    product = models.ManyToManyField(Product,related_name="items")
    refrence = models.ForeignKey(Order, related_name='refrence', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    quantity = models.TextField(null=True, blank=True)
    
    def __str__(self):
        for item in Product.objects.all():
            return item.pr_name


class ShippingAddress(models.Model):
    usr = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.address

# class Transaction(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     token = models.CharField(max_length=120)
#     order_id = models.CharField(max_length=120)
#     amount = models.DecimalField(max_digits=100, decimal_places=2)
#     success = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

#     def __str__(self):
#         return self.order_id

#     class Meta:
#         ordering = ['-timestamp']
