from django.contrib import admin
from .models import Customer, Product, Orders, Tags
from django.forms import CheckboxSelectMultiple
from django.db import models


# Register your models here.


class MyProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register([Customer, Orders, Tags])

admin.site.register(Product, MyProductAdmin)
