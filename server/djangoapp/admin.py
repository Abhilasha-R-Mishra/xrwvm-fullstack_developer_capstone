# from django.contrib import admin
# from .models import related models


# Register your models here.
from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class


# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
