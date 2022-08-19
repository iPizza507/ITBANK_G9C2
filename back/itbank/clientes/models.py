from django.db import models

# Create your models here.


class Cliente (models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_surname = models.CharField(max_length=255)
    customer_dni = models.CharField(max_length=255)
    idBranch = models.ForeignKey(
        "Sucursales.Sucursal", on_delete=models.CASCADE)
    idAdress = models.ForeignKey(
        "Sucursales.ClienteDireccion", on_delete=models.CASCADE)
