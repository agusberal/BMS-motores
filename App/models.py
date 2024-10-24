from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    
    Codigo=models.IntegerField(primary_key=True)
    # Atributos principales
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    version = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    tipo_combustible = models.CharField(max_length=20)
    puertas = models.PositiveIntegerField()
    transmision = models.CharField(max_length=20)
    motor = models.CharField(max_length=20)
    tipo_carroceria = models.CharField(max_length=20)
    kilometros = models.PositiveIntegerField()

    # Atributos de seguridad
    frenos_abs = models.BooleanField(default=False)
    sensor_estacionamiento = models.BooleanField(default=False)
    airbag_conductor = models.BooleanField(default=False)
    airbag_pasajero = models.BooleanField(default=False)
    control_estabilidad = models.BooleanField(default=False)
    traccion_asr = models.BooleanField(default=False)

    # Atributos de confort y conveniencia
    piloto_automatico = models.BooleanField(default=False)
    aire_acondicionado = models.BooleanField(default=False)
    computadora_abordo = models.BooleanField(default=False)
    sensor_lluvia = models.BooleanField(default=False)
    comando_remoto_radio = models.BooleanField(default=False)

    # Atributos de rendimiento y dimensiones
    control_traccion = models.BooleanField(default=False)
    capacidad_personas = models.PositiveIntegerField()
    potencia = models.PositiveIntegerField()  # en caballos de fuerza, por ejemplo
    dimensiones = models.CharField(max_length=50)  # Puede ser un string que represente "Largo x Altura x Ancho"
    distancia_entre_ejes = models.FloatField()  # en metros
    valvulas_por_cilindro = models.PositiveIntegerField()

    # Información general
    direccion = models.CharField(max_length=50)
    alarma = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def __int__(self):
        return self.Codigo