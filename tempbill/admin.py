from django.contrib import admin
from django.template import loader
from django.http import HttpResponse

from .models import Medicine, BillItem, Bill


def print_bills(modeladmin, request, queryset):
    template = loader.get_template('tempbill/index.html')
    return HttpResponse(template.render({'bill_list': queryset}, request));
print_bills.short_description = 'Print Selected Bills'


class BillItemInline(admin.TabularInline):
    model = BillItem


class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_number', 'bill_time', 'total_amount']
    list_filter = ['bill_time', 'total_amount']
    fieldsets = [(None, {'fields': ['bill_number', 'bill_time']})]
    search_fields = ['bill_number']
    actions = [print_bills]
    inlines = [BillItemInline]


admin.site.register(Bill, BillAdmin)
admin.site.register(Medicine)