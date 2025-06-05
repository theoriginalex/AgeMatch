from django.urls import path
from .views import detector_view, detectar_emocion_edad_view
from.import views

urlpatterns = [
    path('detector/', detector_view, name='detector'),
    path('detectar/', detectar_emocion_edad_view, name='detectar_emocion_edad'),
    path('detector/callback/', views.spotify_callback, name='spotify_callback'),
    path('spotify/login/', views.spotify_login, name='spotify_login'),
    path('spotify/reproducir/', views.reproducir_playlist, name='spotify_reproducir'),
    path('spotify/refresh/', views.refresh_spotify_token, name='spotify_refresh'),
    path('spotify_playlist/', views.obtener_playlist, name='spotify_playlist'),


  # <-- Aquí la ruta para login Spotify

]
