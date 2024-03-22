from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cargo(models.Model):
    pick_up_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pick_up_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return self.weight

class Car(models.Model):
    plate_number = models.CharField(max_length=5)
    current_location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    current_location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    carrying_capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return self.plate_number
    
class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField(max_length=20)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)



