from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Sound, Tag
from .forms import SoundForm

import pika
import random


@login_required
def index(request):
    if request.method == 'POST':
        form = SoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    sounds = Sound.objects.all()
    form = SoundForm()
    context = {
        'sounds': sounds,
        'form': form,
    }
    return render(request, 'frontend/index.html', context)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_command_on_queue(request):
    """ Simple code for adding a command onto the queue """
    # TODO check that it is a valid command before putting on queue
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_publish(exchange='',
                          routing_key='commands',
                          body=request.data['command'])
    connection.close()
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
    all_sounds = list(tag.sounds.all())
    random_sound = random.choice(all_sounds)
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_publish(exchange='',
                          routing_key='commands',
                          body=random_sound.command)
    connection.close()
    return Response(request.data)
