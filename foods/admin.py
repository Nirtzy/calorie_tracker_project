from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FoodItem  # Import the FoodItem model from models.py in the same folder

# This line tells the Django admin to create an interface for the FoodItem model.
admin.site.register(FoodItem)