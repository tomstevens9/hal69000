from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-command/', views.put_command_on_queue, name='put-command-on-queue'),
    path('play-random-sound/', views.play_random_sound, name='play-random-sound'),
]
