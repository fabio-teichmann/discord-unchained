from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.getRoutes),
    path("rooms/", view=views.getRooms),
    path("rooms/<str:pk>", view=views.getRoom),
]
