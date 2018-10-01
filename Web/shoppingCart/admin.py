from django.contrib import admin
from shoppingCart import models
# Register your models here.
admin.site.register(models.ProductModel)
admin.site.register(models.OrdersModel)
admin.site.register(models.DetailModel)