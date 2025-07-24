from django.db import models


class FoodItem(models.Model):
    """
    Represents a single food item in the database with its nutritional information per 100g.
    """

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="The name of the food item (e.g., 'Quinoa')."
    )

    # We'll rename this for clarity, but the database column can remain the same for now.
    calories = models.PositiveIntegerField(
        help_text="Calories per 100g."
    )

    # NEW: Field for protein in grams.
    # DecimalField is used for numbers with decimal places.
    # max_digits is the total number of digits allowed (before and after the decimal point).
    # decimal_places is the number of digits to store after the decimal point.
    protein = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Grams of protein per 100g."
    )

    # NEW: Field for fat in grams.
    fat = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Grams of fat per 100g."
    )

    # NEW: Field for carbohydrates in grams.
    carbs = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Grams of carbohydrates per 100g."
    )

    # NEW: Field for fiber in grams.
    fiber = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Grams of fiber per 100g.", default=0.00
    )

    image = models.ImageField(
        upload_to='food_images/',
        blank=True,
        null=True,
        help_text="An optional image for the food item."
    )

    def __str__(self):
        return self.name