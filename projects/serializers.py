# projects/serializers.py

from common.serializers import GenericSerializer
from .models import Project, ProjectMedia
from rest_framework import serializers
from .models import ScopeOfWorks
from media.serializers import MediaSerializer  # Import your MediaSerializer


class ProjectMediaSerializer(serializers.ModelSerializer):
    media = MediaSerializer()  # Use MediaSerializer to serialize media details

    class Meta:
        model = ProjectMedia
        fields = ['media']


class SectorProjectSerializer(GenericSerializer):
    media = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'media']

    def get_media(self, obj):
        # Fetch related media via the intermediary table ProjectMedia
        project_media = ProjectMedia.objects.filter(project=obj, media__cover_photo=True).select_related('media')
        return MediaSerializer([pm.media for pm in project_media], many=True).data


class ScopeOfWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScopeOfWorks
        fields = ['id', 'details']


class ProjectSerializer(serializers.ModelSerializer):
    scope_of_works = ScopeOfWorksSerializer(many=True)
    media = serializers.SerializerMethodField()  # Custom field to handle media through ProjectMedia

    class Meta:
        model = Project
        fields = ['id', 'title', 'value', 'contractor', 'description', 'scope_of_works', 'media']

    def get_media(self, obj):
        # Fetch related media via the intermediary table ProjectMedia
        project_media = ProjectMedia.objects.filter(project=obj).select_related('media')
        return MediaSerializer([pm.media for pm in project_media], many=True).data
