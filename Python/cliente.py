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

    def mostrarDatos(self):
        # al atributo peliculas se le agrega una pelicula
        print('El nombre es: ', self.nombre,
              self.apellido, 'con DNI: ', self.dni)
        for d in self.direccion:
            print('La direccion es:', d)


class Classic(Cliente):
    def __init__(self):
        self.puede_crear_chequera = False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False
        self.cuenta_corriente_negativo = False
        self.limite_de_extraccion = 10000
        self.comision = [1, "%"]
        self.limite_de_transferencia_recibida = 150000

    def __str__(self):
        return '{}, {}'.format(self.puede_crear_chequera, self.puede_crear_tarjeta_credito)


class Gold(Cliente):
    def __init__(self, nombre, apellido, dni, direccion):
        super().__init__(nombre, apellido, dni, direccion)
        self.puede_crear_chequera = True
        self.cantidad_max_chequera = 1
        self.puede_crear_tarjeta_credito = True
        self.cantidad_max_tarjeta_credito = 1
        self.puede_comprar_dolar = True
        self.cuenta_corriente_negativo = -10000
        self.limite_de_extraccion = 20000
        self.comision = [0.5, "%"]
        self.limite_de_transferencia_recibida = 150000

    def __str__(self):
        return '{}, {}'.format(self.puede_crear_chequera, self.puede_crear_tarjeta_credito)


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


dir1 = Direccion("Pampa", "457", "Lanus", "CABA", "Argentina")


#Alejo = Cliente([tipo], [dir1])
# Alejo.mostrarDatos()


tip = input('Classic, Gold o Black? ')
tip = tip.lower()


def crearCliente(n):
    if n == 'classic':
        print('classic')
    elif n == 'gold':
        print('gold')
        # llama a la funcion pedir datos
        pedirDatos()
    elif n == 'black':
        print('black')
    else:
        print('Error! Vuelva a intentar..')


def pedirDatos():
    nombre = input("Cual es el nombre? ")
    #apellido = input("Cual es el apellido? ")
    #dni = input("Cual es el dni? ")
    tipo = Gold(nombre, "Figueroa", "45124451", [dir1])
    tipo.mostrarDatos()


crearCliente(tip)
