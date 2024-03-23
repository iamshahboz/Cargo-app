from rest_framework import serializers 
from .models import Cargo, Car, Location

class CargoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cargo
        fields = ['id','pick_up_location','delivery_location',
                  'weight','description']
        
class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Car 
        fields = ['id','plate_number','current_location','capacity']

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Location
        fields = ['id','city','state','zip_code','latitude','longitude']
        