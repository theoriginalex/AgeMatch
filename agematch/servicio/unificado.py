from deepface import DeepFace

# Detectores en orden: opencv es rápido pero falla con poca luz o rostro inclinado;
# mtcnn y retinaface son más lentos pero mucho más precisos.
DETECTORES = ['opencv', 'mtcnn', 'retinaface']


def _analizar(img_array):
    for detector in DETECTORES:
        try:
            return DeepFace.analyze(
                img_array,
                actions=['age', 'emotion'],
                detector_backend=detector,
                enforce_detection=True
            )[0]  # Tomamos el primer rostro
        except ValueError:
            continue  # No detectó rostro con este detector, probamos el siguiente
    return None


def detectar_emocion_edad(img_array):
    if img_array is None:
        return {'error': 'No se pudo leer la imagen capturada.'}

    try:
        resultado = _analizar(img_array)
        if resultado is None:
            return {'error': 'No se detectó ningún rostro. Mira de frente a la cámara, '
                             'con buena iluminación, e inténtalo de nuevo.'}

        edad = int(resultado['age'])
        emocion = resultado['dominant_emotion'].capitalize()

        traduccion_emociones = {
            'Angry': 'Enojado',
            'Disgust': 'Disgusto',
            'Fear': 'Miedo',
            'Happy': 'Feliz',
            'Sad': 'Triste',
            'Surprise': 'Sorprendido',
            'Neutral': 'Neutral'
        }

        emocion_es = traduccion_emociones.get(emocion, emocion)

        return {
            'edad': edad,
            'emocion': emocion_es
        }

    except Exception as e:
        return {'error': f"No se pudo analizar el rostro: {str(e)}"}

