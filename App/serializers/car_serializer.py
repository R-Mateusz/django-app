from rest_framework import serializers
from App.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_model', 'registration_board', 'registration_start_time', 'registration_end_time', 'parking']