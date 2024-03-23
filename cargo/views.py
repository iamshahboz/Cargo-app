from django.http import HttpResponse
from .serializers import CargoSerializer, CarSerializer, LocationSerializer
from .models import Car, Cargo, Location
from rest_framework import generics

def homepage(request):
    return HttpResponse('<center>This is the Cargo application</center>')


class CargoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all().order_by('-id')
    serializer_class = CargoSerializer

class CarEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car 
    serializer_class = CarSerializer
    

