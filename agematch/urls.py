from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detector/', views.detector_view, name='detector'),
    path('detector/callback/', views.spotify_callback, name='spotify_callback'),
    path('detector/detectar/', views.detectar_emocion_edad_view, name='detectar_emocion'),
    path('detector/spotify/login/', views.spotify_login, name='spotify_login'),
    path('detector/spotify/playlist/', views.obtener_playlist, name='obtener_playlist'),
    path('detector/spotify/reproducir/', views.reproducir_playlist, name='reproducir_playlist'),
    path('detector/spotify/refresh/', views.refresh_spotify_token, name='refresh_token'),
    path('estadisticas/', views.estadisticas_view, name='estadisticas'),
    path('estadisticas', views.estadisticas_view, name='estadisticas'),

]
