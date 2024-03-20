from django.contrib import admin
from .models import Car, Parking


class CarAdmin(admin.ModelAdmin):
    """
    Car model fields and filters
    """
    list_display = ('car_model'
                    , 'parking'
                    , 'registration_board'
                    , 'registration_start_time'
                    , 'registration_end_time'
                    )

    list_filter = ['registration_start_time', 'registration_end_time']


class ParkingAdmin(admin.ModelAdmin):
    """
    Parking model fields and filters
    """
    list_display = ('parking_sector', 'parking_spot')
    list_filter = ['parking_spot', 'parking_sector']


"""
Register models
"""
admin.site.register(Car, CarAdmin)
admin.site.register(Parking, ParkingAdmin)
