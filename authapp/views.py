from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings

from .forms import UserRegistrationForm, CustomPasswordResetForm

# Create your views here.

from django.core.mail import send_mail

from django.core.mail import send_mail
from django.template import loader
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings

from .forms import UserRegistrationForm, CustomPasswordResetForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                send_mail(
                    'Bienvenido/a a AgeMatch',
                    '',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    html_message=loader.render_to_string('authapp/welcome_email.html', {'user': user}),
                    fail_silently=False
                )
                messages.success(request, '¡Registro exitoso! Se ha enviado un correo de bienvenida a tu cuenta.')
            except Exception as e:
                messages.warning(request, f'¡Registro exitoso! Pero hubo un error al enviar el correo: {str(e)}')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'authapp/register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'authapp/password_reset.html'
    success_url = reverse_lazy('auth:password_reset_done')
    email_template_name = 'authapp/password_reset_email.html'
    subject_template_name = 'authapp/password_reset_subject.txt'

from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy

def password_reset_confirm(request, uidb64=None, token=None):
    view = PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('auth:password_reset_complete')
    )
    return view(request, uidb64=uidb64, token=token)

def logout(request):
    auth_logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('auth:register')

class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    redirect_authenticated_user = True  # Redirige a home si ya está autenticado
    next_page = 'home'  # Redirige a home después del login

class CustomPasswordResetView(PasswordResetView):
    template_name = 'authapp/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('auth:password_reset_done')
    email_template_name = 'authapp/password_reset_email.html'
    subject_template_name = 'authapp/password_reset_subject.txt'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authapp/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = CustomPasswordResetForm
