from .models import Parking
from .serializers.parking_serializer import ParkingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ParkingView(APIView):
    """
    class based view
    Inheritance: APIView
    """
    def get_obj(self, pk):
        """
        Retrieve object
        """
        try:
            instance = Parking.objects.get(pk=pk)
            return instance
        except Parking.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        """
        'GET' method
        """
        instance = self.get_obj(pk)
        serializer = ParkingSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk):
        """
        'POST' method
        """
        instance = self.get_obj(pk)
        serializer = ParkingSerializer(data=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        """
        'DELETE' method
        """
        instance = self.get_obj(pk)
        instance.delete()
        return Response(status=204)