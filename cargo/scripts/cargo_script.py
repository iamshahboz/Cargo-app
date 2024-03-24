from cargo.models import Cargo, Location, Car 
from django.db import connection 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

    # available zip codes from db 601, 99929

def run():
    # latitudes = []
    # longtitudes = []
    # cars = Car.objects.all()
    # cargo = Cargo.objects.all()
    # for car in cars:
    #     latitudes.append(f'{car.current_location.latitude}')
    #     longtitudes.append(f'{car.current_location.longitude}')

    # geolocator = Nominatim(user_agent='Cargo_app')
    # for lt, ln in zip(latitudes,longtitudes):
        
    #     location = geolocator.reverse((lt,ln))
    #     print(location)
    cargos = Cargo.objects.all()
    cars = Car.objects.all()
    for cargo in cargos:
        cargo_coordinates = (f'{cargo.pick_up_location.latitude}, {cargo.pick_up_location.longitude}')
    for car in cars:
        car_coordinates = (f'{car.current_location.latitude}, {car.current_location.longitude}')
        distance = geodesic(cargo_coordinates, car_coordinates).miles
        print(distance)




    # coordinates = []
    # cars = Car.objects.all()
    # for car in cars:
    #     coordinates.append(f'{car.current_location.longitude}, {car.current_location.latitude}')
    # print(coordinates)








    # first_location = Location.objects.first()
    # last_location = Location.objects.last()

    # print(first_location.zip_code)
    # print(last_location.zip_code)

    ...

    # first_car = Car.objects.first()
    # longitude = first_car.current_location.longitude
    # latitude = first_car.current_location.latitude
    # geolocator = Nominatim(user_agent='Cargo_app')
    # location = geolocator.reverse((long,lat))
    # print(location)

    # cargo = Cargo.objects.first()
    # print(cargo.zip_c)

