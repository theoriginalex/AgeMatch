import os

base_path = "dataset"

emociones = ["feliz", "triste", "enojado", "sorpresa", "miedo", "disgusto"]
edades = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60+"]

# Crear carpetas
for categoria in emociones:
    os.makedirs(os.path.join(base_path, "emociones", categoria), exist_ok=True)

for categoria in edades:
    os.makedirs(os.path.join(base_path, "edades", categoria), exist_ok=True)

print("Carpetas creadas correctamente.")
