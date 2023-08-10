from django.contrib.auth.models import User
from django.db import models

# For DB table definitions in the form of a Python class that inherits
# from Django Models (django.db.models.Model)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # NOT NULL = False
    # Active users in the room
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    # Take timestamp whenever model gets updated
    updated = models.DateTimeField(auto_now=True)  # takes timestamp every time
    created = models.DateTimeField(auto_now_add=True)  # takes only initial timestamp

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # if room gets deleted, delete all messages
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[:50]
