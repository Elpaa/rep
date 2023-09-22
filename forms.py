from django import forms
from .models import Paciente, LlamadaPaciente, CustomUser

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'fecha_nacimiento', 'direccion', 'telefono', 'email', 'edad']

        widgets = {
            'fecha_nacimiento': forms.TextInput(attrs={'type': 'date'}),
        }

class LlamadaPacienteForm(forms.ModelForm):
    class Meta:
        model = LlamadaPaciente
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'tipo']
        
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)