from django.db import models

class Chip(models.Model):
    numero_chip = models.AutoField(primary_key=True)
    compania = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=100)
    contraseña_plataforma = models.CharField(max_length=100)
    usuario_plataforma = models.CharField(max_length=100)

    def __str__(self):
        return f"Chip {self.numero_chip} - {self.compania}"
