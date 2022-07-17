from asyncio.windows_events import INFINITE


class Classic:
    def __init__(self):
        puede_crear_chequera = False
        puede_crear_tarjeta_credito = False
        puede_comprar_dolar = False
        cuenta_corriente_negativo = False
        retiro_maximo = 10000
        comision = [1, "%"]
        transferencia_maxima = 150000


class Gold:
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


class Black:
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
