from django.db import models

# Create your models here.


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_balance = models.CharField(max_length=30)
    account_iban = models.CharField(max_length=255)
    # decimal_places
    account_limiteExtraccionDiario = models.DecimalField(
        max_digits=5, decimal_places=3)
    account_limiteTransferenciaRecibida = models.DecimalField(
        max_digits=5,  decimal_places=3)
    account_costoTransferenciaRecibida = models.DecimalField(
        max_digits=5, decimal_places=3)
    account_saldoDescubiertoDisponible = models.DecimalField(
        max_digits=5, decimal_places=3)
    account_tipoDeAccount = models.CharField(max_length=255)
    idCustomer = models.ForeignKey(
        "clientes.Cliente", on_delete=models.CASCADE)


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_surname = models.CharField(max_length=255)
    employee_address = models.CharField(max_length=255)
    idBranch = models.ForeignKey(
        "Sucursales.Sucursal", on_delete=models.CASCADE)
    idAddress = models.ForeignKey(
        "Sucursales.ClienteDireccion", on_delete=models.CASCADE)
