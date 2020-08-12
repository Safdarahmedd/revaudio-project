from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SoundSerializer
from .models import Sound
from django.conf import settings
from pydub import AudioSegment
from pathlib import Path
import wave
from datetime import datetime
from django.core.files.storage import FileSystemStorage


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all().order_by('id')
    serializer_class = SoundSerializer

    def perform_create(self, serializer):
        serializer.save()
        sound = Sound.objects.last()
        root = settings.MEDIA_ROOT.replace('/media','')
        loc = root + sound.audio.url
        audiopath = Path(loc)
        clip = AudioSegment.from_wav(audiopath)
        rev = clip.reverse()
        temploc = root + '/media/reversed/'
        now = datetime.now()
        name = now.strftime('%H%M%S_%d_%m_') + 'reversed.wav'
        revpath = Path(temploc+name)
        rev.export(revpath,format='wav')
        fs = FileSystemStorage()
        urlrev = fs.url(name)
        urlrev = urlrev.replace('media/','reversed/')
        sound.reversedaudio = urlrev
        sound.save()
