from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Usuario, LlamadaPaciente
from .forms import PacienteForm, LlamadaPacienteForm, UserRegistrationForm, LoginForm

def index(request):
    pacientes = Paciente.objects.all()
    return render(request, 'layout/base.html', {'pacientes': pacientes})
def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'layout/index.html', {'pacientes': pacientes})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    pacientes = pacientes.order_by('nombre')
    return render(request, 'paciente/lista_pacientes.html', {'pacientes': pacientes})

def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'paciente/detalle_paciente.html', {'paciente': paciente})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente/lista_pacientes')
    else:
        form = PacienteForm()

    return render(request, 'paciente/crear_paciente.html', {'form': form})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente/lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    
    return render(request, 'paciente/editar_paciente.html', {'form': form, 'paciente': paciente})

def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.delete()
    return redirect('paciente/lista_pacientes')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    return render(request, 'usuario/detalle_usuario.html', {'usuario': usuario})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Inicia sesión al usuario después del registro
            login(request, user)
            return redirect('perfil')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'usuario/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuario/perfil.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'usuario/login.html', {'form': form})

def lista_llamadas_pacientes(request):
    llamadas = LlamadaPaciente.objects.all()
    return render(request, 'llamadas/lista_llamadas_pacientes.html', {'llamadas': llamadas})

def crear_llamada_paciente(request):
    if request.method == 'POST':
        form = LlamadaPacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llamadas/lista_llamadas_pacientes')
    else:
        form = LlamadaPacienteForm()
    
    return render(request, 'llamadas/crear_llamada_paciente.html', {'form': form})

def detalle_llamada_paciente(request, llamada_id):
    llamada = get_object_or_404(LlamadaPaciente, pk=llamada_id)
    return render(request, 'llamadas/detalle_llamada_paciente.html', {'llamada': llamada})