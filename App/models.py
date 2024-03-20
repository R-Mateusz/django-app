from django.db import models
from django.utils import timezone

"""
Variables
"""
default_start_time = timezone.now
default_end_time = timezone.now() + timezone.timedelta(days=1)
PARKING_SPOTS = {f"spot_{x}": f"{x}" for x in range(1, 51)}

CAR_MODEL_CHOICES = {"model_bmw": "BMW",
                     "model_audi": "Audi",
                     "model_mercedes": "Mercedes",
                     "model_volvo": "Volvo",
                     "model_toyota": "Toyota"}

PARKING_SECTOR = {"sector_a": "A",
                  "sector_b": "B",
                  "sector_c": "C",
                  "sector_d": "D"}


class Parking(models.Model):
    """
    Parking model
    """
    parking_spot = models.CharField(choices=PARKING_SPOTS, max_length=10)
    parking_sector = models.CharField(choices=PARKING_SECTOR, max_length=10)

    def __str__(self):
        return f"Parking: {PARKING_SECTOR.get(str(self.parking_sector))}{PARKING_SPOTS.get(str(self.parking_spot))}"

    class Meta:
        verbose_name_plural = "Parking"


class Car(models.Model):
    """
    Car model
    """
    car_model = models.CharField(choices=CAR_MODEL_CHOICES, default='model_bmw', blank=False, null=False, max_length=40)
    registration_board = models.CharField(max_length=9, blank=False, null=False, unique=True)
    registration_start_time = models.DateField(default=default_start_time)
    registration_end_time = models.DateField(default=default_end_time)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.registration_board}"

    class Meta:
        verbose_name_plural = "Car"
