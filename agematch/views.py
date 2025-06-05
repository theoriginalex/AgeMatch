from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
from agematch.servicio.unificado import detectar_emocion_edad
from django.http import HttpResponse
from . import views  # Asegúrate de importar las vistas correctamente

def detector_view(request):
    # Renderiza la página con la cámara y botón
    return render(request, 'detector.html')

@csrf_exempt  # Solo para pruebas; luego maneja bien CSRF
def detectar_emocion_edad_view(request):
    if request.method == 'POST':
        imagen = request.FILES.get('imagen')
        if not imagen:
            return JsonResponse({'error': 'No se recibió la imagen'}, status=400)

        file_bytes = np.asarray(bytearray(imagen.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        resultado = detectar_emocion_edad(img)
        return JsonResponse(resultado)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


import requests
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse

CLIENT_ID = '63211bd581204259a19970e080297229'
CLIENT_SECRET = '1737b93ac398442fbdb68418d20fcb92'
REDIRECT_URI = 'http://127.0.0.1:8000/detector/callback/'

def spotify_login(request):
    scope = 'user-read-private user-read-email streaming user-modify-playback-state playlist-read-private'
    auth_url = 'https://accounts.spotify.com/authorize?'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': scope,
        'show_dialog': 'true'
    }

    url = auth_url + urllib.parse.urlencode(params)
    return redirect(url)

def spotify_callback(request):
    # Tu lógica para intercambiar el código por el token de acceso
    return JsonResponse({'mensaje': 'Callback ejecutado correctamente'})


def spotify_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No se recibió el código de autorización desde Spotify.'})

    # Paso 1: Obtener token de acceso
    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    token_response = requests.post(token_url, data=payload)

    if token_response.status_code != 200:
        return JsonResponse({
            'error': 'No se pudo obtener el token de acceso',
            'detalle': token_response.text,
            'status_code': token_response.status_code
        })

    token_data = token_response.json()
    access_token = token_data.get('access_token')
    refresh_token = token_data.get('refresh_token')

    if not access_token:
        return JsonResponse({'error': 'Token de acceso vacío o inválido', 'respuesta': token_data})

    # ✅ Guardar tokens en sesión
    request.session['access_token'] = access_token
    request.session['refresh_token'] = refresh_token

    # Puedes redirigir a cualquier parte de tu app
    return redirect('/detector/')  # o 'return render(...)' si prefieres

from django.http import JsonResponse

def obtener_playlist(request):
    emocion = request.GET.get('emocion')
    if emocion == 'feliz':
        return JsonResponse({
            "url": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
            "genero": "Pop"
        })
    elif emocion == 'triste':
        return JsonResponse({
            "url": "https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA",
            "genero": "Blues"
        })
    else:
        return JsonResponse({"error": "No se encontró una playlist para esa emoción."})


def reproducir_playlist(request):
    playlist_uri = request.GET.get('playlist_uri')
    access_token = request.session.get('spotify_token')  # o donde sea que lo tengas guardado

    if not playlist_uri or not access_token:
        return JsonResponse({'error': 'No se encontró el token o la URI de la playlist'}, status=400)

    # Define el cuerpo de la solicitud
    payload = {
        "context_uri": playlist_uri,
        "offset": {"position": 0},
        "position_ms": 0
    }

    # Enviar la solicitud a Spotify
    response = requests.put(
        'https://api.spotify.com/v1/me/player/play',
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if response.status_code == 204:
        return JsonResponse({'mensaje': 'Reproducción iniciada'})
    else:
        return JsonResponse({'error': response.json()}, status=response.status_code)

def refresh_spotify_token(request):
    refresh_token = request.session.get('refresh_token')
    if not refresh_token:
        return JsonResponse({'error': 'No se encontró el refresh_token en la sesión'}, status=400)

    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    token_response = requests.post(token_url, data=payload)

    if token_response.status_code != 200:
        return JsonResponse({
            'error': 'No se pudo refrescar el token',
            'detalle': token_response.text
        }, status=token_response.status_code)

    token_data = token_response.json()
    new_access_token = token_data.get('access_token')

    # Guardar el nuevo access token en la sesión
    request.session['access_token'] = new_access_token

    return JsonResponse({'access_token': new_access_token, 'mensaje': 'Token actualizado correctamente'})
