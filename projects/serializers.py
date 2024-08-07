# projects/serializers.py

from common.serializers import GenericSerializer
from media.serializers import MediaSerializer
from .models import Project, Media
from rest_framework import serializers


class SectorProjectSerializer(GenericSerializer):
    media = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'media']

    def get_media(self, obj):
        # Filter media to only include cover photos
        media_queryset = obj.media.filter(cover_photo=True)
        #Use GenericSerializer for media
        return GenericSerializer(media_queryset, many=True).data


class ProjectSerializer(GenericSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
