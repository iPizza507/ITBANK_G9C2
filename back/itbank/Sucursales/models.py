from django.db import models

# Create your models here.


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    idAddress = models.ForeignKey(
        "ClienteDireccion", on_delete=models.CASCADE)


class Direcciones(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_calle = models.CharField(max_length=255)
    address_numero = models.CharField(max_length=255)
    address_ciudad = models.CharField(max_length=255)
    address_provincia = models.CharField(max_length=255)
    address_pais = models.CharField(max_length=255)
    idAddress = models.ForeignKey(
        "ClienteDireccion", on_delete=models.CASCADE)


class ClienteDireccion(models.Model):
    ClienteDireccion_id = models.ForeignKey(
        "Direcciones", on_delete=models.CASCADE)
