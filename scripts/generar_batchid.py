import os
from modulos.processes.cplanxgen2_module import cplanxgen2
from modulos.processes.procexgen2_module import procexgen2
from modulos.processes.IDUpdate_module import ID_Update
from modulos.builders.cplanimport_module import cplanimport
from ManageDB.sqlite_on_db import sqlite_Insertar_registro_masivo
from General_Utilities.control_rutas import setting_routes


key = 'databases'
directorio = setting_routes(key)[0]
S_base_datos = directorio + 'vrss_operation_and_managment_subsystem'
S_tabla = '`control_misiones_id_control_process`'

print('{}% Extrayendo la tabla de misiones.'.format(int(0/8*100)))
mode = False
misiones_0 = cplanimport(mode)

dia_de_plan = input('{}% Introducir BatchID: '.format(int(1/8*100)))
Date_Code_BatchID = int(dia_de_plan)

# Aqui generamos el CPLAN
cplanxgen2(misiones_0, Date_Code_BatchID, mode)
# Aqui generamos el resto de los archivos y construimos el arbol de directorios
key = 'plans'
mode = False
container = routing(mode)[key]
procexgen2(container, mode)
# Aqui se construye el dataframe de procesos
df = ID_Update(Date_Code_BatchID, container)
print(df)

pregunta = input('Desea actualizar la tabla de procesos? (S/N): ')

if pregunta == 's' or pregunta == 'S':
    try:
        sqlite_Insertar_registro_masivo(S_base_datos, S_tabla, df, 0, 4)
    except:
        print('No se actualizo la tabla!')