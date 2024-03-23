# import_locations.py

import os
import csv
from django.core.management.base import BaseCommand
from cargo.models import Location  

class Command(BaseCommand):
    help = 'Import locations from a CSV file'

    def handle(self, *args, **options):
        
        file_path = r'C:\Users\hp\Desktop\cargo\app\uszips.csv'
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Location.objects.create(
                    city=row['city'],
                    state=row['state_name'],
                    zip_code=row['zip'],
                    latitude=row['lat'],
                    longitude=row['lng']
                )
        self.stdout.write(self.style.SUCCESS('Locations imported successfully'))
