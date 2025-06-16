from django.core.management.base import BaseCommand
from agematch.models import PlaylistEmocion

class Command(BaseCommand):
    help = 'Agrega playlists predeterminadas para cada emoción'

    def handle(self, *args, **options):
        # Lista de playlists con sus URIs
        playlists = {
            'Enojado': {
                'genero': 'Rock Intenso',
                'uri': 'spotify:playlist:37i9dQZF1DX4dyzvuaRJ0n'  # Rock Intenso
            },
            'Disgusto': {
                'genero': 'Metal',
                'uri': 'spotify:playlist:37i9dQZF1DX894XH637h1w'  # Metal
            },
            'Miedo': {
                'genero': 'Ambient',
                'uri': 'spotify:playlist:37i9dQZF1DX4sWSpwq3LiO'  # Ambient
            },
            'Feliz': {
                'genero': 'Pop',
                'uri': 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'  # Pop
            },
            'Triste': {
                'genero': 'Indie',
                'uri': 'spotify:playlist:37i9dQZF1DX7qK8ma5wgG1'  # Indie
            },
            'Sorprendido': {
                'genero': 'Electrónica',
                'uri': 'spotify:playlist:37i9dQZF1DX4WYpdgoIcn6'  # Electrónica
            },
            'Neutral': {
                'genero': 'Jazz',
                'uri': 'spotify:playlist:37i9dQZF1DX4WYpdgoIcn6'  # Jazz
            }
        }

        # Agregar cada playlist
        for emocion, data in playlists.items():
            playlist, created = PlaylistEmocion.objects.get_or_create(
                emocion=emocion,
                defaults={
                    'genero': data['genero'],
                    'spotify_uri': data['uri']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Playlist agregada: {emocion}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Playlist ya existía: {emocion}'))
