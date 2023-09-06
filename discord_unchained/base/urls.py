# App specific URLs
from django.http import HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    # Rooms
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    # Profiles
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    path("update-user/", views.updateUser, name="update-user"),
    # Messages
    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),
    # Topics
    path("topics/", views.topicsPage, name="topics"),
    # Activities
    path("activities/", views.activityPage, name="activities"),
]
