from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"  # creates form according to all model fields
        # fields = ["name", "body"] # select specific fields
        exclude = ["host", "participants"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        # exclude = []
