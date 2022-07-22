from asyncio.windows_events import INFINITE
from direccion import Direccion
# importar la razon


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str, tipo=[], direccion=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.direccion = direccion
        self.razon = "razon"

    def mostrarNombre(self):
        return print(self.nombre, self.apellido)

    def mostrarDirreccion(self):
        # al atributo peliculas se le agrega una pelicula
        for d in self.direccion:
            print(d)

    def mostrarTipo(self):
        for t in self.tipo:
            print(t)


class Classic(Cliente):
    def __init__(self):
        self.puede_crear_chequera = False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False
        self.cuenta_corriente_negativo = False
        self.limite_de_extraccion = 10000
        self.comision = [1, "%"]
        self.limite_de_transferencia_recibida = 150000

    def mostrarAtributos(self):
        print(self.puede_crear_chequera, self.puede_crear_tarjeta_credito)


class Gold(Cliente):
    def __init__(self):
        self.puede_crear_chequera = True
        self.cantidad_max_chequera = 1
        self.puede_crear_tarjeta_credito = True
        self.cantidad_max_tarjeta_credito = 1
        self.puede_comprar_dolar = True
        self.cuenta_corriente_negativo = -10000
        self.limite_de_extraccion = 20000
        self.comision = [0.5, "%"]
        self.limite_de_transferencia_recibida = 150000

    def mostrarAtributos(self):
        print(self.puede_crear_chequera, self.puede_crear_tarjeta_credito)


class Black(Cliente):
    def __init__(self):
        self.puede_crear_chequera = True
        self.cantidad_max_chequera = 2
        self.puede_crear_tarjeta_credito = True
        self.cantidad_max_tarjeta_credito = 5
        self.puede_comprar_dolar = True
        self.cuenta_corriente_negativo = -10000
        self.limite_de_extraccion = 100000
        self.comision = [0, "%"]
        self.limite_de_transferencia_recibida = INFINITE


tipo = Gold()
dir1 = Direccion("Pampa", "457", "CABA", "Bs As", "Argentina")
Alejo = Cliente("Alejo", "Suarez", "45865442", [tipo], [dir1])

Alejo.mostrarNombre()
Alejo.mostrarDirreccion()
tipo.mostrarAtributos()
