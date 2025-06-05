import os
import cv2
import numpy as np
import os
from keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directorio actual (servicio)
ruta_modelo = os.path.join(BASE_DIR, 'modelo_edades.keras')
modelo_edades = load_model(ruta_modelo)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

# Ruta al dataset de edades
dataset_path = 'dataset/edades'

# Obtener clases (rango de edades)
etiquetas = sorted(os.listdir(dataset_path))
print("Rangos de edad detectados:", etiquetas)

imagenes = []
labels = []

for idx, etiqueta in enumerate(etiquetas):
    carpeta = os.path.join(dataset_path, etiqueta)
    for archivo in os.listdir(carpeta):
        ruta_img = os.path.join(carpeta, archivo)

        # Verifica si la ruta existe
        if not os.path.exists(ruta_img):
            print(f"[X] Archivo no encontrado: {ruta_img}")
            continue

        try:
            imagen = cv2.imread(ruta_img)
            if imagen is not None:
                imagen = cv2.resize(imagen, (64, 64))
                imagenes.append(imagen)
                labels.append(idx)
            else:
                print(f"[!] No se pudo leer la imagen: {ruta_img}")
        except Exception as e:
            print(f"[ERROR] {ruta_img}: {e}")

# Convertir a numpy y normalizar
X = np.array(imagenes, dtype='float32') / 255.0
y = to_categorical(labels)

# Dividir en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Aumentación de datos
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    horizontal_flip=True
)
datagen.fit(X_train)

# Modelo CNN mejorado
modelo = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.25),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.25),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(etiquetas), activation='softmax')
])

# Compilar modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento
modelo.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    epochs=15,
    validation_data=(X_val, y_val)
)

# Guardar modelo en formato moderno
modelo.save('modelo_edades.keras')
print(" Modelo de edades guardado en 'modelo_edades.keras'")
