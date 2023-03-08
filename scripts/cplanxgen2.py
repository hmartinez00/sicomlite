# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Creación: 2022-08-13
# Actualización: 2022-08-19
#
#   Script para generación del CPLAN2.
#
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
import math
import pandas as pd
from datetime import datetime, timedelta

from cplanmodule2 import *
from on_db import *
from extractID import *
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definiendo la Base de datos
# ---------------------------------------------------------------------
base_datos = 'vrss_operation_and_managment_subsystem'

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Consulta a la tabla de Control de Procesos.
#
# Aca se definirá el ID del nuevo plan para insertarlo a la tabla de
# control de procesos de la base de datos.
# ---------------------------------------------------------------------
tabla = '`control_misiones_id_control_process`'
sql = "SELECT * FROM " + tabla + " ORDER BY MessageCreateTime"
Last_MessageID = on_db(base_datos, sql)[-1][1]
Next_MessageID = str(math.ceil(int(Last_MessageID)*0.1)*10).rjust(12, '0')
print('El ID del nuevo proceso sera: ' + Next_MessageID)

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definiendo los valores de fecha del plan y secuencia de workmodes.
# ---------------------------------------------------------------------
print('Solicitando datos iniciales.')

Initial_codes = {}
ImagingList = {}
PlanList = {}
CPLAN_dict = {}

dia_de_plan = input('{}% Introducir BatchID: '.format(int(0/8*100)))

Date_Code_BatchID = int(dia_de_plan)

Initial_codes['MessageID'] = Next_MessageID
Initial_codes['WorkMode'] = ['6', '1', '9']

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Construcción de dataframes
#
# Se construyen los dataframes con los renglones de las misiones 
# que se van a agendar para la fecha intruducida.
# ---------------------------------------------------------------------
print('{}% Creando la tabla de misiones del dia.'.format(int(1/8*100)))
# archivo_0 = \
#     'C:/Users/Hector Martinez/Documents/A - Proyectos/procesamientoXML/' + \
#     'Planes Satelitales 20220817 - 20220823/' + \
#     'Seleccion de misiones/' + \
#     'Simulacion 20220815 1124 - 1.xlsx'
# misiones_0 = pd.read_excel(archivo_0, sheet_name='Progresion de Accesos')

tabla = '`control_misiones_solution_info`'
misiones_0 = mysql_extract_table_df(base_datos, tabla)

misiones_0.columns = [
    'Date', 'Start Time (UTCG)', 'Stop Time (UTCG)', 'Duration (sec)',
    'From Pass', 'To Pass', 'From Start Lat (deg)', 'From Start Lon (deg)',
    'From Start Alt (km)', 'From Stop Lat (deg)', 'From Stop Lon (deg)',
    'From Stop Alt (km)', 'To Start Lat (deg)', 'To Start Lon (deg)',
    'To Start Alt (km)', 'To Stop Lat (deg)', 'To Stop Lon (deg)',
    'To Stop Alt (km)', 'From Pass End', 'To Pass End', 'To Object',
    'From Object', 'To Parent', 'From Parent', 'GLat-Signum', 'GLon-Signum',
    'Inclination', 'Sub-Sat Lat(deg)', 'Sub-Sat Lon(deg)', 'Distance(Km)',
    'Roll Angle (deg)', 'Extension(Km2)', 'HRC/IRC (Teorico)', 'Index'
]

Access = BatchID_missions_table(misiones_0, Date_Code_BatchID)

print(Access)

valores = values_zero(Access, Initial_codes)

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Construyendo los diccionarios de registro.
#
# Desde estos diccionarios es que se volcarán los valores a los
# nuevos XML.
# ---------------------------------------------------------------------
print('{}% Creando el diccionario de registros'.format(int(2/8*100)) + \
    ' para el plan ' + dia_de_plan)

ImagingList['ImagingID'] = valores['ImagingID']
ImagingList['RollAngle'] = valores['RollAngle']
ImagingList['YawAngle'] = valores['YawAngle']
ImagingList['PitchAngle'] = valores['PitchAngle']
ImagingList['FileName'] = valores['FileName']
ImagingList['ImageStartTime'] = valores['ImageStartTime']
ImagingList['ImageEndTime'] = valores['ImageEndTime']

PlanList['PlanID'] = valores['PlanID']
PlanList['SatelliteID'] = valores['SatelliteID']
PlanList['StationID'] = valores['StationID']
PlanList['WorkMode'] = valores['WorkMode']
PlanList['OrbitID'] = valores['OrbitID']
PlanList['CameraID'] = valores['CameraID']
PlanList['TransStartTime'] = valores['TransStartTime']
PlanList['TransEndTime'] = valores['TransEndTime']
PlanList['IsBreakpoint'] = valores['IsBreakpoint']
PlanList['ReplayFile'] = valores['ReplayFile']
PlanList['DeleteFile'] = valores['DeleteFile']
PlanList['ImagingCount'] = valores['ImagingCount']
PlanList['ImagingList'] = ImagingList

CPLAN_dict['MessageID'] = valores['MessageID']
CPLAN_dict['MessageType'] = 'CPLAN2'
CPLAN_dict['Originator'] = 'OMS'
CPLAN_dict['Recipient'] = 'SCC'
CPLAN_dict['MessageCreateTime'] = valores['MessageCreateTime']
CPLAN_dict['TaskID'] = valores['TaskID']
CPLAN_dict['FirstOrbitTime'] = valores['FirstOrbitTime']
CPLAN_dict['OrbitPeriod'] = '5855'
CPLAN_dict['PlanCount'] = valores['PlanCount']
CPLAN_dict['PlanList'] = PlanList

CPLAN_dict['PlanFileName'] = \
    CPLAN_dict['Originator'] + '_' + \
    CPLAN_dict['Recipient'] + '_' + \
    'VRSS-2' + '_' + \
    str(datetime.strftime(
    datetime.strptime(
    CPLAN_dict['MessageCreateTime']
        , '%Y-%m-%dT%H:%M:%S'
    ), '%Y%m%d')) + '_' + \
    CPLAN_dict['MessageID'] + '.' + \
    CPLAN_dict['MessageType']

print('{}% Generando el Plan.'.format(int(3/8*100)))

os.chdir('..')
os.chdir('backup/PMS/')
XML_CPLAN2_generator(CPLAN_dict)

os.chdir('../..')
os.chdir('scripts/')
exec(open('procexgen2.py').read())

print('{}% Actualizando registro de control de procesos.'.format(int(8/8*100)))
IDUpdate(Date_Code_BatchID)