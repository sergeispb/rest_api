from django.contrib import admin
from .models import Product, ProductGroup, Reservation
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(Reservation)
