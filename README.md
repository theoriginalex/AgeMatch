Agematch
  Integrantes

- Elizabeth Pincay
- Alex Chica
-Gabriela Quiyu

 Instrucciones de instalación y ejecución

 1. Clona el repositorio:
```bash
git clone https://github.com/theoriginalex/AgeMatch.git
```

 2. Crea un entorno virtual e instala dependencias:
```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

 3. Configura variables de entorno:
Crea un archivo `.env` con tus claves de Spotify y la base de datos PostgreSQL:

```
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
DATABASE_URL=postgres://usuario:contraseña@localhost:5432/tu_basededatos
```

4. Aplica migraciones y ejecuta el servidor:
```bash
python manage.py migrate
python manage.py runserver
```

# Instalación del frontend (Tailwind CSS)
##  Requisitos

- Python 3.11
- Node.js y npm
- Entorno virtual activado

#  Tener Instalada las dependencias de Python

# Ejecutar estos comando 
# Crear package.json si aún no existe
npm init -y

# Instalar Tailwind CSS y sus herramientas
npm install -D tailwindcss postcss autoprefixer

# Crear el archivo de configuración de Tailwind
npx tailwindcss init

# Compilar el CSS (esto generará static/css/output.css)
npm run build-css



# Descripción del proyecto

Este proyecto usa visión por computadora para detectar emociones humanas a través de la cámara, y según la emoción detectada, recomienda y reproduce automáticamente una playlist de Spotify.

También genera estadísticas por usuario con Power BI para analizar tendencias emocionales, y puede alertar si una emoción negativa persiste (como posible síntoma de depresión).

# Tecnologías utilizadas
Python + Django – Framework principal.

DeepFace – Detección de emociones con IA.

OpenCV – Captura de imagen desde cámara.

Spotify API (OAuth 2.0) – Recomendaciones musicales.

PostgreSQL – Almacenamiento de emociones y usuarios.


HTML, tailwindCSS, JavaScript – Interfaz web.

# Funcionalidades:

- Detección facial y emocional desde la cámara.
- Recomendación musical basada en emoción detectada.
- Reproducción automática de playlist usando la API de Spotify.
- Registro de emociones por usuario.
- Visualización de estadísticas .


**Licencia:** Este proyecto es académico y no tiene fines comerciales.
