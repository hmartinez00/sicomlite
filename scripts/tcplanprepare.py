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
import pandas as pd
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

from V2Gen.procexmodule2 import TCPLAN_extract
# from on_db import *

import mysql.connector

# ---------------------------------------------------------------------

archivo_viejo = input('Introduzca ruta del archivo: ')
print('Archivo: ' + archivo_viejo)

directorio = os.path.dirname(archivo_viejo)
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
    os.path.basename(archivo_viejo.split('.')[0]) + ' ' + \
    satellite + ' ' + dia_inicial + '-' + dia_final + '.xml'

print(archivo_nuevo)

pregunta = input('Desea cambiar la extension del archivo? (S/N): ')

if pregunta == 's' or pregunta == 'S':
     shutil.copy(archivo_viejo, archivo_nuevo)