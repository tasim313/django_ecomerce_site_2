from django.contrib import admin
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'category_name']
    list_filter = ['category_title', 'category_name', 'created_at']
    search_fields = ['category_title', 'category_name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_category',  'product_brand',  'ratings',
                    'created_at', 'slug']
    list_filter = ['product_category', 'product_brand']
    search_fields = ['product_category', 'product_name ', 'product_brand', ' product_price', 'slug']

    prepopulated_fields = {'slug': ('product_category', 'product_name',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'comment']
    list_filter = ['name', 'rating', 'comment']
    search_fields = ['name', 'rating']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['shipping_price', 'delivery_at','created_at']
    list_filter = ['shipping_price', 'delivery_at','created_at']
    search_fields = ['shipping_price', 'delivery_at','created_at']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', '_id']
    list_filter = ['name', 'quantity', '_id']
    search_fields = ['name', 'quantity', '_id']


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'shipping_cost']
    list_filter = ['address',  'shipping_cost']
    search_fields = ['address', 'shipping_cost']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)