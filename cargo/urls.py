from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage, name='homepage'),

    # this api is for creating cargo
    path('cargo/create/',views.CargoCreateView.as_view()),

    # this one is to list(read) created cargo with needed fields
    path('cargo/',views.CargoList.as_view()),

    # getting cargo by id and editing
    path('cargo/<int:pk>/',views.CargoEdit.as_view()),

    # editing car by id 
    path('car/<int:pk>/',views.CarEdit.as_view()),

    # getting all cars
    path('car/',views.CarList.as_view()),


]