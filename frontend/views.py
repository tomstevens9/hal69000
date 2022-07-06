from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView

from django.shortcuts import render

from .models import Sound, Tag, SoundHistory
from .serializers import SoundSerializer, CommandSerializer, TagSerializer

import magic
import pika
import random

# Unused in React version
"""
@login_required
def index(request):
    if request.method == 'POST':
        form = SoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
"""

# TODO
# * Handle file upload


# React app
def index(request):
    return render(request, "frontend/index.html")


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]


class SoundListView(generics.ListAPIView):
    queryset = Sound.objects.all()
    serializer_class = CommandSerializer


@api_view(["GET"])
def get_popular_tags(request):
    popular_tags = SoundHistory.get_popular_tags()
    serializer = TagSerializer(popular_tags, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def upload_sound(request):
    data = {
        "command": request.POST["command"],
        "filename": request.FILES["file"],
        "tags": None,
    }
    serializer = SoundSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Command saved")
    return Response(
        "Failed to upload sound", status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )


@api_view(["GET"])
@renderer_classes([StaticHTMLRenderer])
@permission_classes([AllowAny])
def get_sound(request, command):
    mime = magic.Magic(mime=True)
    sound = Sound.objects.get(command=command)
    return Response(
        sound.filename.read(), content_type=mime.from_file(str(sound.filename.file))
    )


@api_view(["POST"])
def put_command_on_queue(request):
    """Simple code for adding a command onto the queue"""
    command = request.data["command"]  # TODO validate
    # Check that the sound exists.
    # Currently this will crash and return a 500 on error.
    # TODO Could add better error handling
    sound = Sound.objects.get(command=command)
    # Send the command to rabbit to be processed by the bot.
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="commands")
    channel.basic_publish(exchange="", routing_key="commands", body=command)
    connection.close()
    # Record that the sound has been played.
    SoundHistory.objects.create(sound=sound)
    return Response(request.data)


@api_view(["POST"])
def play_random_sound(request):
    """Plays a random sound with a given tag"""
    # Get tag
    tag_name = request.data["tag_name"]
    tag = Tag.objects.get(name=tag_name)
    # Find a random sound for a tag
    all_sounds = tag.sound_set.all()
    random_sound = random.choice(all_sounds)
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="commands")
    channel.basic_publish(
        exchange="", routing_key="commands", body=random_sound.command
    )
    connection.close()
    # Record that the sound has been played.
    SoundHistory.objects.create(sound=random_sound)
    return Response(request.data)
