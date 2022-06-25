from django.contrib import admin

from .models import Sound, Tag, SoundHistory

admin.site.register(Sound)
admin.site.register(Tag)
admin.site.register(SoundHistory)
