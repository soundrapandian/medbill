from django.db import models


class TaxGroup(models.Model):
    name = models.CharField(max_length=30)


class Tax(models.Model):
    name = models.CharField(max_length=30)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    tax_group = models.ForeignKey(TaxGroup)