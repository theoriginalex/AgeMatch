from django.db import models

# Create your models here.
class PlaylistEmocion(models.Model):
    emocion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    spotify_uri = models.CharField(max_length=100)  # URI de la playlist

    def __str__(self):
        return f"{self.emocion} - {self.genero}"


from django.contrib.auth.models import User

class RegistroEmocion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    emocion = models.CharField(max_length=50)
    edad = models.IntegerField(default=25)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.emocion} ({self.fecha.strftime('%Y-%m-%d %H:%M')})"