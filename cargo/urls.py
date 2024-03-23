from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('cargo/<int:pk>/',views.CargoEdit.as_view()),
    path('car/<int:pk>/',views.CarEdit.as_view()),

]