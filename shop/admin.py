from django.contrib import admin

from .models import Shop, Supplier, ItemCategory, Item, ItemStockBatch, ShopEmployee


class ShopEmployeeInline(admin.TabularInline):
    model = ShopEmployee


class ShopSupplier(admin.TabularInline):
    model = Supplier


class ShopItemCategory(admin.TabularInline):
    model = ItemCategory


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state']
    list_filter = ['name', 'city', 'state']
    inlines = [ShopEmployeeInline, ShopSupplier, ShopItemCategory]


admin.site.register(Shop, ShopAdmin)
admin.site.register(Item)
admin.site.register(ItemStockBatch)
