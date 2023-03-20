# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
import shutil
from datetime import datetime
from V2Gen.procexmodule2 import TCPLAN_extract
from modulos.processes.routing_module import routing


def tcplanprepare(mode):

    '''
    ABAE-SAT-UT-SGO
    Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
    Creación: 2022-10-12
    Actualización: 2022-10-12
    
    tcplanprepare: Script para preparacion del TCPLAN.

    '''

    key = 'missions'
    directorio = routing(mode)[key]
    print(directorio)

    rutas = []
    for nombre_directorio, dirs, ficheros in os.walk(directorio):
        for nombre_fichero in ficheros:
            if '.txt' in nombre_fichero:
                ruta = nombre_directorio + '\\' + nombre_fichero
                rutas.append(ruta.replace('\\', ''))

    archivo_viejo = rutas[-1]
    print(archivo_viejo)

    satellite = TCPLAN_extract(archivo_viejo)['SCNAME'][0]

    dia_inicial = datetime.strftime(
        datetime.strptime(
            TCPLAN_extract(archivo_viejo)['FileTS'][0]
            , '%Y-%m-%d %H:%M:%S.%f'
        ), '%Y%m%d')

    dia_final = datetime.strftime(
        datetime.strptime(
            TCPLAN_extract(archivo_viejo)['FileTE'][0]
            , '%Y-%m-%d %H:%M:%S.%f'
        ), '%Y%m%d')

    print(satellite, dia_inicial, dia_final)

    archivo_nuevo = directorio + '\\' + \
        os.path.basename(archivo_viejo.split('.')[0]) + '_' + \
        satellite + '_' + dia_inicial + '-' + dia_final + '.xml'

    print(archivo_nuevo)

    pregunta = input('Desea cambiar la extension del archivo? (S/N): ')

    if pregunta == 's' or pregunta == 'S':
        shutil.copy(archivo_viejo, archivo_nuevo)