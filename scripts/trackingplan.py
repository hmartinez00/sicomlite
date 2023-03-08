# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Creación: 2022-08-20
# Actualización: 2022-08-29
#
#   Script para actualizacion del TCPLAN.
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
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

# ---------------------------------------------------------------------
# Recabando info de XMLs.
# ---------------------------------------------------------------------
os.chdir('..')
directorio = 'backup\\TCPLAN\\'
rutas = []

for nombre_directorio, dirs, ficheros in os.walk(directorio):
    for nombre_fichero in ficheros:
        if '.xml' in nombre_fichero:
            ruta = nombre_directorio + '\\' + nombre_fichero
            rutas.append(ruta.replace('\\', '/'))

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Levantando el Dataframe General.

# Este segmento organiza en un Dataframe toda la informacion
# que se encuentra almacenada en los archivos XML del directorio
# TCPLAN.
# ---------------------------------------------------------------------
vdf = []
for i in range(len(rutas)):
    vdf.append(pd.DataFrame(TCPLAN_extract(rutas[i])))

df = pd.concat(vdf).sort_values('TTS')


df = df[
    [   
        'MadeTime',
        'SCNAME',
        'DEVNAME',
        'REVNUM',
        'MAXE',
        'TTS',
        'TTE',
        'TTSL',
        'TTEL'
    ]
]


df['Index'] = [i for i in range(len(df))]

df.set_index('Index',inplace=True)
df.index.name = None

df.columns = [
    'MadeTime',
    'SCName',
    'DevName',
    'OrbitID', 
    'MaxElev',
    'CaptureStartTime',
    'CaptureEndTime',
    'StartLocalTime',
    'EndLocalTime',
]

df['CaptureStartTime'] = pd.to_datetime(df['CaptureStartTime'])

repeticiones = []
for i in range(len(df)):
    for j in range(len(df)):
        if i != j:
            if df['OrbitID'][i] == df['OrbitID'][j]:
                fecha_actualizada = min(df['MadeTime'][i], df['MadeTime'][j])
                if df['MadeTime'][i] == fecha_actualizada:
                    repeticiones.append(i)

no_repeticiones = []
for i in range(len(df)):
    if i in repeticiones:
        continue
    else:
        no_repeticiones.append(i)

df = df.iloc[no_repeticiones]

df = df[[
    'SCName',
    'DevName',
    'OrbitID', 
    'MaxElev',
    'CaptureStartTime',
    'CaptureEndTime',
    'StartLocalTime',
    'EndLocalTime',
    'MadeTime',
]]

df[df.index.name] = [i for i in range(len(df))]
df.set_index(df.index.name,inplace=True)
df.index.name = None

# Reporte de fechas extremales.
print(
        [
            df['CaptureStartTime'].min(),
            df['CaptureStartTime'].max()
        ]
    )

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Segmentando la informacion a ingresar
# ---------------------------------------------------------------------
__BatchID__A = input('Introduzca BatchID inicial: ')
__BatchID__B = input('Introduzca BatchID final: ')
delay = timedelta(hours=4, minutes=40)
delay_day = timedelta(days=1, hours=4, minutes=40)
__diaA__ = datetime.strptime(__BatchID__A, '%Y%m%d') + delay
__diaB__ = datetime.strptime(__BatchID__B, '%Y%m%d') + delay_day

df = df[
    (df['CaptureStartTime'] >= __diaA__) & \
    (df['CaptureStartTime'] <= __diaB__)
]

df[df.index.name] = [i for i in range(len(df))]
df.set_index(df.index.name,inplace=True)
df.index.name = None

print(df)

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Ingresando a la Base de datos
# ---------------------------------------------------------------------

# base_datos = 'vrss_operation_and_managment_subsystem'
# tabla = '`control_misiones_tcplan_info`'

# pregunta = input('Desea ingresar la informacion a la Base de datos? (s/n): ')

# if pregunta == 's' or pregunta == 'S':
#     Insertar_registro_masivo(df, base_datos, tabla)
# elif pregunta == 'n' or pregunta == 'N':
#     print('No se ingreso informacion!' + '\n')
# else:
#     print('Opción inválida!' + '\n')
