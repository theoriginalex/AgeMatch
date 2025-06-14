Agematch
  Integrantes

- Elizabeth Pincay
- Alex Chica
-Gabriela Quiyu

 Instrucciones de instalación y ejecución

 1. Clona el repositorio:
```bash
git clone https://github.com/theoriginalex/AgeMatch.git
cd proyecto-emociones
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

# Descripción del proyecto

Este proyecto usa visión por computadora para detectar emociones humanas a través de la cámara, y según la emoción detectada, recomienda y reproduce automáticamente una playlist de Spotify.

También genera estadísticas por usuario con Power BI para analizar tendencias emocionales, y puede alertar si una emoción negativa persiste (como posible síntoma de depresión).

# Tecnologías utilizadas
Python + Django – Framework principal.

DeepFace – Detección de emociones con IA.

OpenCV – Captura de imagen desde cámara.

Spotify API (OAuth 2.0) – Recomendaciones musicales.

PostgreSQL – Almacenamiento de emociones y usuarios.

Power BI – Visualización de estadísticas.

HTML, CSS, JavaScript – Interfaz web.

# Funcionalidades:

- Detección facial y emocional desde la cámara.
- Recomendación musical basada en emoción detectada.
- Reproducción automática de playlist usando la API de Spotify.
- Registro de emociones por usuario.
- Visualización de estadísticas con Power BI integradas en Django.

# Visualización de Power BI

Se incluye un iframe que muestra estadísticas emocionales personalizadas directamente en la web del usuario.



**Licencia:** Este proyecto es académico y no tiene fines comerciales.
