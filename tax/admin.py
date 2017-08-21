from django.contrib import admin

from .models import TaxGroup, Tax


class TaxInline(admin.TabularInline):
    model = Tax


class TaxGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    inlines = [TaxInline]


admin.site.register(TaxGroup, TaxGroupAdmin)
