from rest_framework import serializers

from .models import Sound

class SoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sound
        fields = ('name', 'audio', 'reversedaudio')
