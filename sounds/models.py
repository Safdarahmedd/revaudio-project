from django.db import models

class Sound(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    audio = models.FileField(upload_to='original/')
    reversedaudio = models.FileField(upload_to='reversed/', null=True, blank=True)

    def __str__(self):
        return str(self.id) + '_' + self.name
