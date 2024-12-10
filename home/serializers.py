from rest_framework import serializers
from main.models import *

class BlackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Black
        fields = ['id', 'img', 'color', 'frame']

class WhiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Black
        fields = ['id', 'img', 'color', 'frame']