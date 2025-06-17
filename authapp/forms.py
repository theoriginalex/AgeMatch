from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User

# Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nombre de usuario',
            'autofocus': True,
            'autocomplete': 'username',
            'aria-label': 'Nombre de usuario',
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password',
            'aria-label': 'Contraseña',
        })
    )

# Registro
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nombre de usuario',
            'autofocus': True,
            'autocomplete': 'username',
        })
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        help_text='Requerido. Ingrese un correo electrónico válido.',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email',
            'aria-describedby': 'emailHelp',
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Contraseña',
            'autocomplete': 'new-password',
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirmar contraseña',
            'autocomplete': 'new-password',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Reset de contraseña
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email',
            'aria-label': 'Correo electrónico',
        })
    )

# Cambio de contraseña
class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Contraseña actual',
            'autocomplete': 'current-password',
        })
    )
    new_password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nueva contraseña',
            'autocomplete': 'new-password',
        })
    )
    new_password2 = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirmar nueva contraseña',
            'autocomplete': 'new-password',
        })
    )
