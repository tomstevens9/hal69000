from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-command/', views.put_command_on_queue, name='put-command-on-queue'),
]
