from rest_framework import serializers

from .models import Sound, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class SoundSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Sound
        fields = [
            "command",
            "filename",
            "tags",
        ]


class CommandSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Sound
        fields = [
            "command",
            "tags",
        ]
