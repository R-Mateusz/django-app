from django.urls import path
from . import views, views_parking


urlpatterns = [
    path('Car/', views.get_obj),
    path('Car/<int:pk>/', views.obj_detail),
    path('Parking/', views_parking.ParkingView.as_view()),
    path('Parking/<int:pk>', views_parking.ParkingView.as_view())
]