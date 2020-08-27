from rest_framework import serializers
from .models import Abstract, Street, Scenic, Message

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abstract
        fields = ('src', 'thumbnail', 'thumbnailWidth', 'thumbnailHeight', 'margin')

class ScenicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenic
        fields = ('src', 'thumbnail', 'thumbnailWidth', 'thumbnailHeight', 'margin')

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('src', 'thumbnail', 'thumbnailWidth', 'thumbnailHeight', 'margin')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')


