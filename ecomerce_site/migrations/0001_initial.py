# Generated by Django 3.1.7 on 2021-04-02 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_icon', models.FileField(blank=True, default='def.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=50)),
                ('category_name', models.CharField(max_length=50)),
                ('cat_details', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('payment_method', models.CharField(blank=True, max_length=200, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('shipping_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('isDelivered', models.BooleanField(default=False)),
                ('delivery_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-isDelivered'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.FileField(upload_to='')),
                ('product_description', models.TextField(null=True, verbose_name='Description')),
                ('product_price', models.FloatField(verbose_name='Price')),
                ('product_old_price', models.FloatField(default=0.0, verbose_name='Previous Price')),
                ('ratings', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='ecomerce_site.brand')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='ecomerce_site.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=20)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomerce_site.order')),
            ],
            options={
                'ordering': ['-_id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomerce_site.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomerce_site.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomerce_site.product')),
            ],
        ),
    ]
