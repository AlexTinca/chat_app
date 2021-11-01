from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    title = models.CharField(max_length=20)


class Participant(models.Model):
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)


class Message(models.Model):
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
