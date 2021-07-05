from rest_framework import serializers
from pydub import AudioSegment
from django.conf import settings
import os
from django.core.files import File as DjangoFile
from .models import Sound, RevSound



class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('name', 'audio')

    def create(self, validated_data):
        sound = Sound.objects.create(**validated_data)
        clip = AudioSegment.from_wav(sound.audio)
        temp_path = settings.MEDIA_ROOT + 'temp.wav'
        rev = clip.reverse()
        id = sound.id
        root = settings.MEDIA_ROOT 
        root = root + 'temp.wav'
        rev.export(root,format='wav')
        print(temp_path)
        temp = DjangoFile(open(temp_path, mode='rb'), name='temp.wav')
        x = {'og':id, 'reversedaudio':temp}
        revserial = RevSerializer(data=x)
        if revserial.is_valid():
            r = revserial.save()
            if os.path.isfile(temp_path):
                os.remove(temp_path)
        else:
            print (revserial.errors)

        return {
            'RevAudio': r.reversedaudio.url 
        }


class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevSound
        fields = ('og', 'reversedaudio')