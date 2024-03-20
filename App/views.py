from rest_framework.parsers import JSONParser
from .models import Car
from .serializers.car_serializer import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def get_obj(request):
    """
    Get all objects
    """
    if request.method == 'GET':
        instance = Car.objects.all()
        serializer = CarSerializer(instance, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['GET', 'POST', 'DELETE'])
def obj_detail(request, pk):
    """
    Get specific object
    """
    try:
        instance = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instance.delete()
        return Response(status=204)