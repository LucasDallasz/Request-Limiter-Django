from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Senha',
        max_length=50,
        strip=False,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        max_length=50,
        strip=False,
        widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ['username']
        
    
class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=150,
    )
    password = forms.CharField(
        label='Senha',
        max_length=50,
        strip=False,
        widget=forms.PasswordInput()
    )