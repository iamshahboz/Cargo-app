from django.http import HttpResponse
from .serializers import CargoSerializer, CarSerializer, LocationSerializer
from .models import Car, Cargo, Location
from rest_framework import generics
from rest_framework.response import Response

def homepage(request):
    return HttpResponse('<center>This is the Cargo application</center>')

class CargoCreateView(generics.CreateAPIView):
    queryset = Cargo.objects.all().order_by('-id')
    serializer_class = CargoSerializer


class CargoList(generics.ListAPIView):
    queryset = Cargo.objects.all().order_by('-id')
    serializer_class = CargoSerializer
    filterset_fields = ['weight',]   




class CargoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cargo.objects.all().order_by('-id')
    serializer_class = CargoSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CarList(generics.ListAPIView):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer

class CarEdit(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)






    



    

