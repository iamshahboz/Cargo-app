from rest_framework import serializers 
from .models import Cargo, Car, Location
from geopy.distance import geodesic


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Location
        fields = ['id','city','state','zip_code','latitude','longitude']


class CargoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    pick_up_zip_code = serializers.IntegerField(write_only=True)
    delivery_zip_code = serializers.IntegerField(write_only=True)
    pick_up_location = serializers.SerializerMethodField()
    delivery_location = serializers.SerializerMethodField()
    nearest_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('id','pick_up_zip_code', 'delivery_zip_code', 'pick_up_location', 'delivery_location', 'weight', 'description','nearest_cars')

    def get_pick_up_location(self, obj):
        return {
            "city": obj.pick_up_location.city,
            "state": obj.pick_up_location.state,
            "zip_code": obj.pick_up_location.zip_code,
            "latitude": str(obj.pick_up_location.latitude),
            "longitude": str(obj.pick_up_location.longitude)
        }

    def get_delivery_location(self, obj):
        return {
            "city": obj.delivery_location.city,
            "state": obj.delivery_location.state,
            "zip_code": obj.delivery_location.zip_code,
            "latitude": str(obj.delivery_location.latitude),
            "longitude": str(obj.delivery_location.longitude)
        }
    
    def get_nearest_cars(self,obj):
        # cargo coordinates
        cargo_coordinates = (obj.delivery_location.latitude, obj.delivery_location.longitude)
        
        count = 0
        # car coordinats


        cars = Car.objects.all()
        for car in cars:
            car_coordinates = (car.current_location.latitude, car.current_location.longitude)
            distance = geodesic(cargo_coordinates,car_coordinates).miles
            if distance <= 450:
                count +=1
        return count


    def create(self, validated_data):
        pick_up_zip_code = validated_data.pop('pick_up_zip_code')
        delivery_zip_code = validated_data.pop('delivery_zip_code')
        try:
            pick_up_location = Location.objects.get(zip_code=pick_up_zip_code)
            delivery_location = Location.objects.get(zip_code=delivery_zip_code)

            cargo = Cargo.objects.create(pick_up_location=pick_up_location, delivery_location=delivery_location, **validated_data)
            return cargo
        except Location.DoesNotExist:
            raise serializers.ValidationError("Zip code not found")


        
class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    current_location = serializers.SerializerMethodField()
    class Meta:
        model = Car 
        fields = ['id','plate_number','current_location','capacity']

    def get_current_location(self,obj):
        return {
            "city": obj.current_location.city,
            "state": obj.current_location.state,
            "zip_code": obj.current_location.zip_code,
            "latitude": obj.current_location.latitude,
            "longitude": obj.current_location.longitude


        }
    



        