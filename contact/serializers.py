
from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()