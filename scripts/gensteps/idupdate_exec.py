from modulos.processes.IDUpdate_module import ID_Update
from modulos.processes.routing_module import routing
from ManageDB.sqlite_on_db import sqlite_Insertar_registro_masivo


key = 'database'
mode = False
directorio = routing(mode)[key]
S_base_datos = directorio + 'vrss_operation_and_managment_subsystem'
S_tabla = '`control_misiones_id_control_process`'


key = 'plans'
mode = False
container = routing(mode)[key]

dia_de_plan = input('{}% Introducir BatchID: '.format(int(0/8*100)))

Date_Code_BatchID = int(dia_de_plan)

df = ID_Update(Date_Code_BatchID, container)
print(df)


pregunta = input('Desea actualizar la tabla de procesos? (S/N): ')

if pregunta == 's' or pregunta == 'S':
    try:
        sqlite_Insertar_registro_masivo(S_base_datos, S_tabla, df, 0, 4)
    except:
        print('No se actualizo la tabla!')