from django.db import models
from django.contrib.auth.models import User

from tax.models import TaxGroup

class Organization(models.Model):
    name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default='India')
    pin = models.CharField(max_length=6)
    phone1 = models.CharField(max_length=15, null=True)
    phone2 = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=15, null=True)

    def __str__(self):
        return '{0} - {1}, {2}'.format(self.name, self.city, self.state)

    class Meta:
        abstract = True


class Shop(Organization):
    active = models.BooleanField()


class Supplier(Organization):
    shop = models.ForeignKey(Shop)


class ShopEmployee(models.Model):
    shop = models.ForeignKey(Shop)
    employee = models.ForeignKey(User)


class ItemCategory(models.Model):
    name = models.CharField(max_length=30)
    shop = models.ForeignKey(Shop)
    tax = models.ForeignKey(TaxGroup, null=True)


class Item(models.Model):
    category = models.ForeignKey(ItemCategory)
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=30)
    tax = models.ForeignKey(TaxGroup, null=True)


class ItemStockBatch(models.Model):
    item = models.ForeignKey(Item)
    shop = models.ForeignKey(Shop)
    batch_id = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier)
    unit_cost = models.PositiveIntegerField()
    purchased_stock = models.PositiveIntegerField()
    purchased_date = models.DateField()
    expiry_date = models.DateField()
    current_stock = models.PositiveIntegerField()
    tax = models.ForeignKey(TaxGroup, null=True)
