# importar la direccion
from direccion import Direccion
from cuenta import Cuenta
# importar la razon

# importar los 3 tipos de clientes
from clases import Black
from clases import Gold
from clases import Classic


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = Direccion()
        self.razon = "razon"
        self.cuenta = Cuenta()

    def mostrarNombre(self):
        return print(self.nombre, self.apellido)

    def get_PuedeCrearChequera(self):
        return self.puede_crear_chequera

    def get_CantidadMaxChequera(self):
        return self.cantidad_max_chequera

    def get_PuedeCrearTarjetaCredito(self):
        return self.puede_crear_tarjeta_credito

    def get_CantidadMaxTarjetaCredito(self):
        return self.cantidad_max_tarjeta_credito

    def get_PuedeComprarDolar(self):
        return self.puede_comprar_dolar

    def get_CuentaCorrienteNegativo(self):
        return self.cuenta_corriente_negativo

    def get_RetiroMaximo(self):
        return self.retiro_maximo

    def get_Comision(self):
        return self.comision

    def get_TransferenciaMaxima(self):
        return self.transferencia_maxima


class Classic(Cliente):
    def __init__(self):
        puede_crear_chequera = False
        puede_crear_tarjeta_credito = False
        puede_comprar_dolar = False
        cuenta_corriente_negativo = False
        retiro_maximo = 10000
        comision = [1, "%"]
        transferencia_maxima = 150000


class Gold(Cliente):
    def __init__(self):
        puede_crear_chequera = True
        cantidad_max_chequera = 1
        puede_crear_tarjeta_credito = True
        cantidad_max_tarjeta_credito = 1
        puede_comprar_dolar = True
        cuenta_corriente_negativo = -10000
        retiro_maximo = 20000
        comision = [0.5, "%"]
        transferencia_maxima = 150000


class Black(Cliente):
    def __init__(self):
        puede_crear_chequera = True
        cantidad_max_chequera = 2
        puede_crear_tarjeta_credito = True
        cantidad_max_tarjeta_credito = 5
        puede_comprar_dolar = True
        cuenta_corriente_negativo = -10000
        retiro_maximo = 100000
        comision = [0, "%"]
        transferencia_maxima = INFINITE
