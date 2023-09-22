from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    edad = models.PositiveIntegerField(default=0)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Area(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[('Administrador', 'Administrador'), ('Generico', 'Generico')])
    
    def __str__(self):
        return self.user.username

class CustomUser(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=20, choices=[('Administrador', 'Administrador'), ('Generico', 'Generico')])

    custom_groups = models.ManyToManyField(Group, related_name='custom_users')
    custom_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    groups = None
    user_permissions = None

    def __str__(self):
        return self.username
    
class LlamadaPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_hora_llamada = models.DateTimeField(auto_now_add=True)
    origen_llamada = models.CharField(max_length=20, choices=[('Cuarto', 'Cuarto'), ('Baño', 'Baño')])
    tipo_llamada = models.CharField(max_length=20, choices=[('Normal', 'Normal'), ('Emergencia', 'Emergencia')])
    atendida = models.BooleanField(default=False)

    def __str__(self):
        return f"Llamada de {self.paciente} el {self.fecha_hora_llamada}"
