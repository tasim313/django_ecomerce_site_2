from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50, null=False)
    cat_details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Category Title : {self.category_title} ,Category Name : {self.category_name}, Category Details : {self.cat_details}"

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    brand_name = models.CharField(max_length=100, null=False)
    brand_icon = models.FileField(null=True, blank=True, default="def.png")


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='category')
    product_name = models.CharField(max_length=100, null=False)
    product_image = models.FileField()
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='brand')
    product_description = models.TextField(null=True, verbose_name='Description')
    product_price = models.FloatField(verbose_name='Price')
    product_old_price = models.FloatField(default=0.0, verbose_name="Previous Price")
    ratings = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"Product Category: {self.product_category}, Product Name: {self.product_name}, " \
               f"Product Image:{self.product_image},Product Brand={self.product_brand}, " \
               f"Product Description:{self.product_description}, Product Price:{self.product_price}," \
               f"Product Previous Price:{self.product_old_price}, Rating:{self.ratings}, Reviews:{self.num_reviews}," \
               f"Slug{self.slug}"

    class Meta:
        ordering = ['-created_at',]


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return f'Name:{self.name}, Rating:{self.rating}'

    class Meta:
        ordering = ['-created_at',]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    delivery_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'Created at:{self.created_at}, Shipping Price:{self.shipping_price}, ' \
               f'Payment Method:{self.payment_method}'

    class Meta:
        ordering = ['-created_at', '-delivery_at',]


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'Name:{self.name}, Quantity:{self.quantity},Price:{self.price}'


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    shipping_cost = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'Address:{self.address},Id:{self._id}'

    class Meta:
        ordering = ['-_id',]



