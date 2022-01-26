from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Sound
from .forms import SoundForm

import pika

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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_command_on_queue(request):
    # Simple code for adding a command onto the queue
    # TODO check that it is a valid command before putting on queue
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='commands')
    channel.basic_publish(exchange='',
                          routing_key='commands',
                          body=request.data['command'])
    connection.close()
    return Response(request.data)
