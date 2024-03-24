import random 
from celery import shared_task
from django.utils import timezone 
from cargo.models import Car, Location 

@shared_task
def update_car_location():
    cars = Car.objects.all()
    locations = Location.objects.all()

    for car in cars:
        new_location = random.choice(locations)
        car.current_location = new_location
        car.save()
        