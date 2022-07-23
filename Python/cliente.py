from asyncio.windows_events import INFINITE
from xmlrpc.client import boolean
from direccion import Direccion
# importar la razon


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str, direccion=[], razon=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.razon = razon

    def mostrarDatosCliente(self):
        # al atributo peliculas se le agrega una pelicula
        print('--------------LOS DATOS DEL CLIENTE SON--------------')
        print('El nombre es: ', self.nombre, self.apellido)
        print('con DNI: ', self.dni)
        for d in self.direccion:
            print('La direccion es:', d)


class Classic(Cliente):
    def __init__(self, nombre, apellido, dni, direccion):
        super().__init__(nombre, apellido, dni, direccion)
        self.puede_crear_chequera = False
        self.puede_crear_tarjeta_credito = False
        self.puede_comprar_dolar = False
        self.cuenta_corriente_negativo = False
        self.limite_de_extraccion = 10000
        self.comision = [1, "%"]
        self.limite_de_transferencia_recibida = 150000

    def mostrarDatosClassic(self):
        print('--------------DATOS Classic--------------')
        print('Puede crear chequera?', self.puede_crear_chequera)
        print('Cantidad maxima de chequera:', self.cantidad_max_chequera)
        print('Puede tener tarjeta de credito?',
              self.puede_crear_tarjeta_credito)
        print('Cantidad maxima de tarjetas de credito? ',
              self.cantidad_max_tarjeta_credito)
        print('Puede comprar dolar? ', self.puede_comprar_dolar)
        print('Cuenta corriente negativo máximo:',
              self.cuenta_corriente_negativo)
        print('Limite de extraccion diaria?', self.limite_de_extraccion)
        print('Comision', self.comision)
        print('Limite de transferencia recibida:',
              self.limite_de_transferencia_recibida)


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

    def mostrarDatosGold(self):
        print('--------------DATOS GOLD--------------')
        print('Puede crear chequera?', self.puede_crear_chequera)
        print('Cantidad maxima de chequera:', self.cantidad_max_chequera)
        print('Puede tener tarjeta de credito?',
              self.puede_crear_tarjeta_credito)
        print('Cantidad maxima de tarjetas de credito? ',
              self.cantidad_max_tarjeta_credito)
        print('Puede comprar dolar? ', self.puede_comprar_dolar)
        print('Cuenta corriente negativo máximo:',
              self.cuenta_corriente_negativo)
        print('Limite de extraccion diaria?', self.limite_de_extraccion)
        print('Comision', self.comision)
        print('Limite de transferencia recibida:',
              self.limite_de_transferencia_recibida)


class Black(Cliente):
    def __init__(self, nombre, apellido, dni, direccion):
        super().__init__(nombre, apellido, dni, direccion)
        self.puede_crear_chequera = True
        self.cantidad_max_chequera = 2
        self.puede_crear_tarjeta_credito = True
        self.cantidad_max_tarjeta_credito = 5
        self.puede_comprar_dolar = True
        self.cuenta_corriente_negativo = -10000
        self.limite_de_extraccion = 100000
        self.comision = [0, "%"]
        self.limite_de_transferencia_recibida = INFINITE

    def mostrarDatosBlack(self):
        print('--------------DATOS BLACK--------------')
        print('Puede crear chequera?', self.puede_crear_chequera)
        print('Cantidad maxima de chequera:', self.cantidad_max_chequera)
        print('Puede tener tarjeta de credito?',
              self.puede_crear_tarjeta_credito)
        print('Cantidad maxima de tarjetas de credito? ',
              self.cantidad_max_tarjeta_credito)
        print('Puede comprar dolar? ', self.puede_comprar_dolar)
        print('Cuenta corriente negativo máximo:',
              self.cuenta_corriente_negativo)
        print('Limite de extraccion diaria?', self.limite_de_extraccion)
        print('Comision', self.comision)
        print('Limite de transferencia recibida:',
              self.limite_de_transferencia_recibida)


# array para guardar todos los clientes
clientesClassic = []
clientesGold = []
clientesBlack = []

# depende qué tipo de cliente quiere ser, se creará


def crearTipoCliente(n):
    if n == 'classic':
        dir1 = Direccion("Pampa", "457", "Lanus", "CABA", "Argentina")
        clientesClassic.append(Classic("Ian", "Figueroa", "45124451", [dir1]))
        for cli in clientesClassic:
            cli.mostrarDatosCliente()
            cli.mostrarDatosClassic()
        masClientes()

    elif n == 'gold':
        dir1 = Direccion("Pampa", "457", "Lanus", "CABA", "Argentina")
        clientesGold.append(Gold("Ian", "Figueroa", "45124451", [dir1]))
        for cli in clientesGold:
            cli.mostrarDatosCliente()
            cli.mostrarDatosGold()
        masClientes()

    elif n == 'black':
        dir1 = Direccion("Pampa", "457", "Lanus", "CABA", "Argentina")
        clientesBlack.append(Black("Ian", "Figueroa", "45124451", [dir1]))
        for cli in clientesBlack:
            cli.mostrarDatosCliente()
            cli.mostrarDatosBlack()
        masClientes()

    else:
        print('Error! Vuelva a intentar..')
        masClientes()

# Agregar o no mas clientes


def masClientes():
    respuesta = input("Desea agregar más clientes? Y/N: ").upper()
    if respuesta == "Y":
        tipoDeCliente = input('Classic, Gold o Black? ').lower()
        crearTipoCliente(tipoDeCliente)
    elif respuesta == "N":
        print("cierra App")
    else:
        print("No te entendi, disculpame..")
        masClientes()


masClientes()
