from rest_framework import serializers 
from .models import Cargo, Car, Location

class CargoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cargo
        fields = ['id','pick_up_longitude','pick_up_latitude',
                  'delivery_longitude','delivery_latitude','weight','description']
        
class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Car 
        fields = ['id','plate_number','current_location_longitude','current_location_latitude','carrying_capacity']

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Location
        fields = ['id','city','state','zip_code','longitude','latitude']
        