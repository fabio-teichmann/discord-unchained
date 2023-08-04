from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RoomForm
from .models import Room

# rooms = [
#     {"id": 1, "name": "Let's learn Python"},
#     {"id": 2, "name": "Design with me"},
#     {"id": 3, "name": "Frontend developers"},
# ]


# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in Room.objects.all():
    #     if i["id"] == int(pk):
    #         room = i

    context = {"room": room}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)
