# from django.http import JsonResponse
from base.models import Room
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RoomSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = ["GET /api", "GET /api/rooms", "GET /api/rooms/:id"]
    return Response(routes)


@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getRoom(request, pk):
    try:
        room = Room.objects.get(id=pk)

    except ObjectDoesNotExist:
        # Dummy object if id is not valid
        room = {"name": None}

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
