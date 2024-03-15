from django.contrib import admin
from .models import Car, Parking


"""
    Setup models with filters
"""
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['registration_board'
        , 'registration_start_time'
        , 'registration_end_time'

                    ,'parking_spot_car'
                    ]

    list_filter = ['registration_start_time', 'registration_end_time']


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['parking_sector', 'parking_spot']

    list_filter = ['parking_spot', 'parking_sector']

    ordering = ['parking_sector', 'parking_spot']


