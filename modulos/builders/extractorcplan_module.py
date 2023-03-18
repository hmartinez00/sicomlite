import os
import pandas as pd
from datetime import datetime
from modulos.processes.routing_module import routing


def extractorcplan(mode):
    '''
    ABAE-SAT-UT-SGO
    Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
    Creación: 2022-08-25
    Actualización: 2022-08-25
      Script para extraccion del plan de misiones con exportacion
      a *.csv.
    '''

    key = 'missions'
    # mode = True
    directorio = routing(mode)[key]
    rutas = []

    for nombre_directorio, dirs, ficheros in os.walk(directorio):
        for nombre_fichero in ficheros:
            if 'final.xlsx' in nombre_fichero:
                ruta = nombre_directorio + '\\' + nombre_fichero
                rutas.append(ruta.replace('\\', ''))


    # archivo_0 = input('Introduzca ruta del archivo: ')
    archivo_0 = rutas[-1]
    print(archivo_0)

    tiempo = datetime.strftime(
        datetime.now()
        , '%Y%m%d%H%M%S'
    )

    misiones_0 = pd.read_excel(archivo_0, sheet_name='Progresion de Accesos')

    cabeceras = {}
    cabeceras[misiones_0.columns[32]] = 'HRC/IRC (Teorico)'

    misiones_0 = misiones_0.rename(
        columns = cabeceras
    )

    return misiones_0