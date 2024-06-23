from django.contrib import admin

from stock.models import Product, MeasureUnit

admin.site.register(Product)
admin.site.register(MeasureUnit)
