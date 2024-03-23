# myapp/management/commands/create_cars.py

import random
from django.core.management.base import BaseCommand
from cargo.models import Car, Location

class Command(BaseCommand):
    help = 'Creates 20 records for the Car model'

    def handle(self, *args, **kwargs):
        plate_numbers = self.generate_plate_numbers(20)
        locations = Location.objects.order_by('?')[:20]  # Select 20 random locations from the database

        for i in range(20):
            car = Car.objects.create(
                plate_number=plate_numbers[i],
                current_location=locations[i],
                capacity=random.randint(1, 1000)  # Assuming capacity is a random value
            )
            self.stdout.write(self.style.SUCCESS(f'Created Car: {car}'))

    def generate_plate_numbers(self, count):
        plate_numbers = []
        for _ in range(count):
            plate_number = f'{random.randint(1000, 9999)}{random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}'
            plate_numbers.append(plate_number)
        return plate_numbers
