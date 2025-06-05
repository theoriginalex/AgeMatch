import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directorio actual (servicio)

etiquetas_edad = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
etiquetas_emocion = ['Enojado', 'Desagrado', 'Miedo', 'Feliz', 'Triste', 'Sorprendido', 'Neutral']

# Configurar detector de rostros con OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detectar_emocion_edad(img_array):
    # Convertir a escala de grises para la detección de rostros
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros usando OpenCV
    rostros = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(rostros) == 0:
        return {'error': 'No se detectó rostro'}
    
    # Procesar el primer rostro detectado
    (x, y, w, h) = rostros[0]
    rostro = img_array[y:y+h, x:x+w]
    
    # Análisis simple basado en características faciales
    # Esto es una versión simplificada que no requiere modelos de aprendizaje profundo
    # La edad se estima basada en el tamaño del rostro (los niños tienen rostros más pequeños)
    # La emoción se estima basada en la simetría del rostro
    
    # Estimación simple de edad basada en tamaño
    if w < 80:
        edad = '0-9'
    elif w < 100:
        edad = '10-19'
    elif w < 120:
        edad = '20-29'
    elif w < 140:
        edad = '30-39'
    elif w < 160:
        edad = '40-49'
    else:
        edad = '50+'
    
    # Estimación simple de emoción basada en simetría
    # Convertir a escala de grises y calcular simetría
    gray_rostro = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)
    flip = cv2.flip(gray_rostro, 1)
    diff = cv2.absdiff(gray_rostro, flip)
    simetria = np.mean(diff)
    
    if simetria < 10:  # Rostro simétrico
        emocion = 'Neutral'
    elif simetria < 20:
        emocion = 'Feliz'
    else:
        emocion = 'Enojado'
    
    return {
        'edad': edad,
        'emocion': emocion
    }


