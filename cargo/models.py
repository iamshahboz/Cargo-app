from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.zip_code
    

class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, related_name='pick_up_cargos',on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(Location,related_name='delivery_cargos',on_delete=models.CASCADE)
    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()

    def __str__(self):
        return self.weight


class Car(models.Model):
    plate_number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, related_name='car_location', on_delete=models.CASCADE)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

    # def __str__(self):
    #     return self.capacity
    
    




