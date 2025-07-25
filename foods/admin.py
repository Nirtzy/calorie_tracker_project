from django.contrib import admin
from .models import FoodItem, UserProfile  # Import the FoodItem and UserProfile models from models.py in the same folder

# This line tells the Django admin to create an interface for the FoodItem and UserProfile models.
admin.site.register(FoodItem)
admin.site.register(UserProfile)
