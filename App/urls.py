from django.urls import path
from . import views_car, views_parking


urlpatterns = [
    path('Car/', views_car.get_obj),
    path('Car/<int:pk>/', views_car.obj_detail),
    path('Parking/', views_parking.ParkingView.as_view()),
    path('Parking/<int:pk>', views_parking.ParkingDetailView.as_view())
]