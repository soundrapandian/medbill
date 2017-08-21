from django.db import models
from decimal import Decimal


class Medicine(models.Model):
    name = models.CharField(max_length=30)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{0} (Rs. {1})'.format(self.name, self.unit_cost)


class Bill(models.Model):
    bill_number = models.CharField(max_length=30)
    bill_time = models.DateTimeField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return '{0} (Total Rs. {1})'.format(self.bill_number, self.total_amount)

    def save(self, *args, **kwargs):
        super(Bill, self).save(*args, **kwargs)
        self.total_amount = Decimal(0.0)
        for bill_item in self.items():
            self.total_amount += bill_item.medicine.unit_cost * bill_item.number
        super(Bill, self).save(*args, **kwargs)

    def items(self):
        return BillItem.objects.filter(bill=self.pk)

    def time(self):
        return self.bill_time.strftime('%H:%M:%S')

    def date(self):
        return self.bill_time.strftime('%d:%m:%Y')

    def grand_total(self):
        return '{0}0'.format(self.total_amount.__round__(1))

    def round_off(self):
        return (self.total_amount - self.total_amount.__round__(1)).__round__(2)


class BillItem(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=None)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.medicine, self.number)

    def cost(self):
        return self.medicine.unit_cost * self.number
