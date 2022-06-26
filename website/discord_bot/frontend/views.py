from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Sound, Tag, SoundHistory
from .forms import SoundForm

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

    sounds = Sound.objects.all()
    popular_tags = SoundHistory.get_popular_tags()
    form = SoundForm()
    context = {
        'sounds': sounds,
        'form': form,
        'popular_tags': popular_tags,
    }
    return render(request, 'index.html', context)
"""

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_command_on_queue(request):
    """ Simple code for adding a command onto the queue """
    command = request.data['command']  # TODO validate
    # Check that the sound exists.
    # Currently this will crash and return a 500 on error.
    # TODO Could add better error handling
    sound = Sound.objects.get(command=command)
    # Send the command to rabbit to be processed by the bot.
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_publish(exchange='',
                          routing_key='commands',
                          body=command)
    connection.close()
    # Record that the sound has been played.
    SoundHistory.objects.create(sound=sound)
    return Response(request.data)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def play_random_sound(request):
    """ Plays a random sound with a given tag """
    # Get tag
    tag_name = request.data['tag_name']
    tag = Tag.objects.get(name=tag_name)
    # Find a random sound for a tag
    all_sounds = tag.sound_set.all()
    random_sound = random.choice(all_sounds)
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_publish(exchange='',
                          routing_key='commands',
                          body=random_sound.command)
    connection.close()
    return Response(request.data)
