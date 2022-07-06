from django.urls import path
from knox import views as knox_views
from django.contrib import admin

from . import views

urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"admin/", admin.site.urls),
    path(r"auth/login/", views.LoginView.as_view(), name="knox_login"),
    path(r"auth/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(r"auth/logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path(r"upload-sound/", views.upload_sound, name="upload-sound"),
    path(r"sound/<str:command>/", views.get_sound, name="get-sound"),
    path(r"sounds/", views.SoundListView.as_view(), name="sounds"),
    path(r"popular-tags/", views.get_popular_tags, name="popular-tags"),
    path(r"send-command/", views.put_command_on_queue, name="put-command-on-queue"),
    path(r"play-random-sound/", views.play_random_sound, name="play-random-sound"),
]
