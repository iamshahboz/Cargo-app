from django.http import HttpResponse
from .serializers import CargoSerializer, CarSerializer, LocationSerializer
from .models import Car, Cargo, Location

def homepage(request):
    return HttpResponse('<center>This is the Cargo application</center>')

