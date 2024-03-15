from django.db import models
from django.utils import timezone

"""
    Variables
"""

default_start_time = timezone.now
default_end_time = timezone.now() + timezone.timedelta(days=1)
CAR_MODEL_CHOICES = {"model_bmw": "BMW",
                     "model_audi": "Audi",
                     "model_mercedes": "Mercedes",
                     "model_volvo": "Volvo",
                     "model_toyota": "Toyota"}

PARKING_SPOTS = {f"spot_{x}": f"{x}" for x in range(1, 51)}

PARKING_SECTOR = {"sector_a": "A",
                  "sector_b": "B",
                  "sector_c": "C",
                  "sector_d": "D"}
parking_spot_tmp = 0
"""
    Methods
"""


def parm_Parking_obj(obj):
    parking_spot_tmp = obj
    return parking_spot_tmp

"""
    Models initialization for parking reservation app
"""


class Parking(models.Model):
    parking_spot = models.CharField(choices=PARKING_SPOTS, max_length=10)
    parking_sector = models.CharField(choices=PARKING_SECTOR, max_length=10)

    #parking_spot_tmp = parm_Parking_obj(parking_spot)
    def __str__(self):
        return f"Parking: {PARKING_SECTOR.get(str(self.parking_sector))}{PARKING_SPOTS.get(str(self.parking_spot))}"
    class Meta:
        verbose_name_plural = "Parking"





class Car(models.Model):
    car_model = models.CharField(choices=CAR_MODEL_CHOICES, default='model_bmw', blank=False, null=False, max_length=40)
    registration_board = models.CharField(max_length=9, blank=False, null=False)
    registration_start_time = models.DateField(default=default_start_time)
    registration_end_time = models.DateField(default=default_end_time)

    parking_spot_car = parking_spot_tmp





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        used_parking = Car.objects.exclude(parking=None).values_list('parking')
        self._meta.get_field('parking').choices= [(parking.pk, str(parking)) for parking in Parking.objects.exclude(pk__in=used_parking)]

    parking = models.OneToOneField(Parking, on_delete=models.PROTECT, null=False, blank=False, default=None)



    class Meta:
        verbose_name_plural = "Car"

