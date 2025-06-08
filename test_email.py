from django.core.mail import send_mail
from django.conf import settings

# Configuración de correo
settings.configure(
    DEBUG=True,
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend',
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_PORT=587,
    EMAIL_USE_TLS=True,
    EMAIL_HOST_USER='tu.correo@gmail.com',
    EMAIL_HOST_PASSWORD='contraseña_de_aplicación',
    DEFAULT_FROM_EMAIL='AgeMatch <tu.correo@gmail.com>',
)

# Intentar enviar un correo de prueba
try:
    send_mail(
        'Prueba de correo',
        'Este es un correo de prueba para verificar que el sistema de correo funcione.',
        settings.DEFAULT_FROM_EMAIL,
        ['tu.correo@gmail.com'],
        fail_silently=False,
    )
    print("Correo enviado exitosamente!")
except Exception as e:
    print(f"Error al enviar correo: {str(e)}")
