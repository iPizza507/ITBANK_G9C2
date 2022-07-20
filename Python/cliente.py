# importar la direccion
from asyncio.windows_events import INFINITE
from direccion import Direccion
# importar la razon


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str, direccion=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.razon = "razon"
        self.tipo = ""

    def mostrarNombre(self):
        return print(self.nombre, self.apellido)

    def mostrar(self):
        # al atributo peliculas se le agrega una pelicula
        for d in self.direccion:
            print(d)

    def tipo(self, tipo):
        # GOLd ---> gold
        tipo = tipo.lower()
        if tipo == "gold":
            return Gold()
        if tipo == "black":
            return Black()
        if tipo == "classic":
            return Classic()
        if tipo == "":
            return "default"


class Classic(Cliente):
    def __init__(self):
        puede_crear_chequera = False
        puede_crear_tarjeta_credito = False
        puede_comprar_dolar = False
        cuenta_corriente_negativo = False
        limite_de_extraccion = 10000
        comision = [1, "%"]
        limite_de_transferencia_recibida = 150000


class Gold(Cliente):
    def __init__(self):
        puede_crear_chequera = True
        cantidad_max_chequera = 1
        puede_crear_tarjeta_credito = True
        cantidad_max_tarjeta_credito = 1
        puede_comprar_dolar = True
        cuenta_corriente_negativo = -10000
        limite_de_extraccion = 20000
        comision = [0.5, "%"]
        limite_de_transferencia_recibida = 150000


class Black(Cliente):
    def __init__(self):
        puede_crear_chequera = True
        cantidad_max_chequera = 2
        puede_crear_tarjeta_credito = True
        cantidad_max_tarjeta_credito = 5
        puede_comprar_dolar = True
        cuenta_corriente_negativo = -10000
        limite_de_extraccion = 100000
        comision = [0, "%"]
        limite_de_transferencia_recibida = INFINITE


dir1 = Direccion("pampa", "457", "CABA", "Bs As", "Argentina")
Alejo = Cliente("Alejo", "Suarez", "45865442", [dir1])

Alejo.mostrar()
Alejo.mostrarNombre()
