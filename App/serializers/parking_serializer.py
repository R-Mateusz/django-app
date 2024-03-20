from rest_framework import serializers
from App.models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['id', 'parking_spot', 'parking_sector']
