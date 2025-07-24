from django.core.management.base import BaseCommand
from foods.models import FoodItem
import csv
from decimal import Decimal

class Command(BaseCommand):
    help = 'Import foods from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        count = 0
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cleaned_row = {key.strip(): value for key, value in row.items()}
                try:
                    if not FoodItem.objects.filter(name=cleaned_row['food']).exists():
                        FoodItem.objects.create(
                            name=cleaned_row['food'],
                            calories=Decimal(cleaned_row['Caloric Value']),
                            carbs=Decimal(cleaned_row['Carbohydrates']),
                            fat=Decimal(cleaned_row['Fat']),
                            fiber=Decimal(cleaned_row['Dietary Fiber']),
                            protein=Decimal(cleaned_row['Protein']),
                        )
                        count += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"❌ Error on row {cleaned_row.get('food', 'Unknown')}: {e}"))
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} new food items.'))