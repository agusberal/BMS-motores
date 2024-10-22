from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    """
    Modelo que representa un vehículo para la venta.
    """

    # Datos generales del vehículo
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    color = models.CharField(max_length=20)

    # Características del vehículo
    tipo = models.CharField(max_length=20, choices=[
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Camioneta', 'Camioneta'),
    ])
    transmision = models.CharField(max_length=20, choices=[
        ('Automática', 'Automática'),
        ('Manual', 'Manual'),
    ])
    combustible = models.CharField(max_length=20, choices=[
        ('Gasolina', 'Gasolina'),
        ('Diesel', 'Diesel'),
        ('Híbrido', 'Híbrido'),
        ('Eléctrico', 'Eléctrico'),
    ])

    # Datos de venta
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    kilometraje = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    ])

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def __int__(self):
        return self.id