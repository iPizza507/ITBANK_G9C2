from django.db import models

# Create your models here.


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_tpye = models.CharField(max_length=11)
    loan_date = models.CharField(max_length=10)
    # decimal_places
    loan_total = models.DecimalField(max_digits=30, decimal_places=2)
    idCustomer = models.ForeignKey(
        "clientes.Cliente", on_delete=models.CASCADE)
