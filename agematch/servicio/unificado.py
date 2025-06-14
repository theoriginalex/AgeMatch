from deepface import DeepFace

def detectar_emocion_edad(img_array):
    try:
        resultado = DeepFace.analyze(
            img_array,
            actions=['age', 'emotion'],
            enforce_detection=True
        )[0]  # Tomamos el primer rostro

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

