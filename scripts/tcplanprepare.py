# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Creación: 2022-10-12
# Actualización: 2022-10-12
#
#   Script para preparacion del TCPLAN.
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
import shutil
from datetime import datetime
from V2Gen.procexmodule2 import TCPLAN_extract
from modulos.processes.routing_module import routing


# ---------------------------------------------------------------------

key = 'missions'
directorio = routing(key)[1]
print(directorio)

archivo_viejo = input('Introduzca ruta del archivo: ')
print('Archivo: ' + archivo_viejo)

directorio = os.path.dirname(archivo_viejo)
print(directorio)
print('Directorio del archivo: ' + directorio)

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