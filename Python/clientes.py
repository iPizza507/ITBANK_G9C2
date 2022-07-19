from cuenta import Cuenta 
from direccion import Direccion
from clases import Black
class Cliente:
    def __init__(self, nombre:str, apellido:str, dni:str, direccion:Direccion, razon, cuenta:Cuenta, puede_crear_chequera, cantidad_max_chequera, puede_crear_tarjeta_credito, cantidad_max_tarjeta_credito,puede_comprar_dolar, cuenta_corriente_negativo, retiro_maximo, comision, transferencia_maxima):
        self.nombre = nombre
        self.apellido= apellido
        self.dni = dni
        self.direccion = direccion
        self.razon = razon
        self.cuenta = cuenta
        self.puede_crear_chequera = puede_crear_chequera
        self.cantidad_max_chequera = cantidad_max_chequera
        self.puede_crear_tarjeta_credito = puede_crear_tarjeta_credito
        self.cantidad_max_tarjeta_credito = cantidad_max_tarjeta_credito
        self.puede_comprar_dolar = puede_comprar_dolar
        self.cuenta_corriente_negativo = cuenta_corriente_negativo
        self.retiro_maximo = retiro_maximo
        self.comision = comision
        self.transferencia_maxima = transferencia_maxima
    
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
        return  self.cuenta_corriente_negativo
    
    def get_RetiroMaximo(self):
        return self.retiro_maximo
    
    def get_Comision(self):
        return self.comision
    
    def get_TransferenciaMaxima(self):
        return self.transferencia_maxima