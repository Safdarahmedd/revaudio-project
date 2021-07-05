from django.db import models

class Sound(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    audio = models.FileField()

    def __str__(self):
        return str(self.id) + '_' + self.name

class RevSound(models.Model):
    og = models.OneToOneField(Sound, on_delete=models.CASCADE, primary_key=True)
    reversedaudio = models.FileField() 