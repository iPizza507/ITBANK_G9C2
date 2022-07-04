from ast import If
import sys
import csv
import datetime

# variables del input del usuario
POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_NUMERO = 3
# variables de mi BDD
ETIQUETA_CABECERA_CSV_DNI = 'DNI'
ETIQUETA_CABECERA_CSV_NUM_CHEQUE = 'NroCheque'
ETIQUETA_CABECERA_CSV_FECHA = 'Fecha'
ETIQUETA_CABECERA_CSV_CUENTA = 'NroCuentaOrigen'
ETIQUETA_CABECERA_CSV_CUENTA_DESTINO = 'NroCuentaDestino'
ETIQUETA_CABECERA_CSV_CODIGO_BANCO = 'CodigoBanco'
ETIQUETA_CABECERA_CSV_CODIGO_SUCURSAL = 'CodigoSucursal'
ETIQUETA_CABECERA_CSV_VALOR = 'Valor'
ETIQUETA_CABECERA_CSV_ESTADO = 'Estado'

# lo que se va a ejecutar - MAIN
if __name__ == '__main__':
    # abrir el archivo
    with open(sys.argv[POSICION_ARGUMENTO_NOMBRE_ARCHIVO]) as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)
        cabecera = datos[0]
    (
        posicion_dni,
        posicion_numero,
        posicion_fecha,
        posicion_estado
    ) = (
        cabecera.index(ETIQUETA_CABECERA_CSV_DNI),
        cabecera.index(ETIQUETA_CABECERA_CSV_NUM_CHEQUE),
        cabecera.index(ETIQUETA_CABECERA_CSV_FECHA),
        cabecera.index(ETIQUETA_CABECERA_CSV_ESTADO)
    )

    valor = input("Elige: Pantalla o CSV")
    valor = valor.lower()

    if(valor == "pantalla"):
        datos_cliente = list(filter(
            lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
        print(','.join(cabecera))

        for dato in datos_cliente:
            print(','.join(dato))
    elif(valor == "csv"):
        archivoNuevo = open(
            f"{posicion_dni}{str(datetime.datetime.now()).replace(':','_')}.csv", "x")

        '''
        for item in datos:
            newitem = item(filter(
                lambda registro: registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
            print(newitem)
        '''
        print(type(datos))
        archivoNuevo.write(str(datos))
        archivoNuevo.close()
    else:
        print("Error")
