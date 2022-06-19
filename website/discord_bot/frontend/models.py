from django.db import models


class Sound(models.Model):
    command = models.CharField(max_length=30)
    filename = models.FileField(max_length=30)


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sounds = models.ManyToManyField(Sound)
