import os
from modulos.processes.cplanxgen2_module import cplanxgen2
from modulos.processes.procexgen2_module import procexgen2
from modulos.processes.IDUpdate_module import ID_Update
from modulos.builders.cplanimport_module import cplanimport
from ManageDB.sqlite_on_db import sqlite_Insertar_registro_masivo


S_base_datos = 'vrss_operation_and_managment_subsystem'
S_tabla = '`control_misiones_id_control_process`'

print('{}% Extrayendo la tabla de misiones.'.format(int(0/8*100)))
misiones_0 = cplanimport()

dia_de_plan = input('{}% Introducir BatchID: '.format(int(1/8*100)))
Date_Code_BatchID = int(dia_de_plan)

# Aqui generamos el CPLAN
cplanxgen2(misiones_0, Date_Code_BatchID)
# Aqui generamos el resto de los archivos y construimos el arbol de directorios
procexgen2()
# Aqui se construye el dataframe de procesos
df = ID_Update(Date_Code_BatchID)
print(df)

pregunta = input('Desea actualizar la tabla de procesos? (S/N): ')

if pregunta == 's' or pregunta == 'S':
    try:
        os.chdir('../..')
        sqlite_Insertar_registro_masivo(S_base_datos, S_tabla, df, 0, 4)
    except:
        print('No se actualizo la tabla!')