# importar la direccion
from direccion import Direccion

# importar la razon

# importar los 3 tipos de clientes
from clases import Black
from clases import Gold
from clases import Classic


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str, direccion: Direccion, razon,):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.razon = razon
        self.cuenta = "Aca va la cuenta"

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
