import os
import cv2
import numpy as np
import os
from keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directorio actual (servicio)
ruta_modelo = os.path.join(BASE_DIR, 'modelo_edades.keras')
modelo_edades = load_model(ruta_modelo)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

def cargar_datos(data_dir, img_size):
    etiquetas = sorted(os.listdir(data_dir))
    print("Etiquetas detectadas:", etiquetas)

    X = []
    y = []

    for idx, etiqueta in enumerate(etiquetas):
        ruta = os.path.join(data_dir, etiqueta)
        contador = 0
        for archivo in os.listdir(ruta):
            if not archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
            img_path = os.path.join(ruta, archivo)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                try:
                    img = cv2.resize(img, (img_size, img_size))
                    X.append(img)
                    y.append(idx)
                    contador += 1
                except Exception as e:
                    print(f"[!] Error procesando {img_path}: {e}")
            else:
                print(f"[!] No se pudo leer la imagen: {img_path}")
        print(f"  - {etiqueta}: {contador} imágenes válidas")
    
    return np.array(X), np.array(y), etiquetas

def construir_modelo(input_shape, num_classes):
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2,2)),
        Dropout(0.25),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D((2,2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == '__main__':
    data_dir = 'dataset/emociones'
    img_size = 48

    X, y, etiquetas = cargar_datos(data_dir, img_size)
    X = X.reshape(-1, img_size, img_size, 1) / 255.0
    y = to_categorical(y, num_classes=len(etiquetas))

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = construir_modelo((img_size, img_size, 1), len(etiquetas))

    model.fit(X_train, y_train, epochs=15, batch_size=32, validation_data=(X_val, y_val))

    model.save('modelo_emociones.keras')
    print(" Modelo de emociones guardado como 'modelo_emociones.keras'")

