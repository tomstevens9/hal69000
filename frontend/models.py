from django.db import models

from collections import defaultdict


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Sound(models.Model):
    command = models.CharField(max_length=30)
    filename = models.FileField(max_length=30)
    tags = models.ManyToManyField(Tag)


class SoundHistory(models.Model):
    sound = models.ForeignKey(Sound, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)

    # TODO should maybe be defined somewhere else
    @classmethod
    def get_popular_tags(cls):
        sound_histories = cls.objects.all()
        # Count how often each tag is used
        tag_counts = defaultdict(int)
        for sound_history in sound_histories:
            sound = sound_history.sound
            for tag in sound.tags.all():
                tag_counts[tag] += 1
        # Order tags by most played
        tags = (pair[0]
                for pair
                in sorted(tag_counts.items(),
                          key=lambda x: x[1],
                          reverse=True))
        return tags
