from modulos.processes.tcplanprepare_module import tcplanprepare
from modulos.builders.cplanimport_module import cplanimport
from modulos.processes.cplanxgen2_module import cplanxgen2
from modulos.processes.procexgen2_module import procexgen2
from modulos.processes.routing_module import routing
from modulos.processes.IDUpdate_module import ID_Update
from ManageDB.sqlite_on_db import sqlite_Insertar_registro_masivo


def generar_TCPLAN(mode_0):
    '''
    Actualiza la extension del TCPLAN. Por defecto es entregada en *.txt. Esta funcion transforma dicha extension a *.xml.
    '''

    tcplanprepare(mode_0)

def generar_CPLAN(mode_0):
    '''
    Funcion de gestion de generacion del CPLAN.
    
    **parametros:
        mode_0: bool. Modo de interaccion con "cplanimport". Cuando es True solicita confirmacion de la ruta de archivos a consultar. Cuando vale False, acude a la ruta del compendio mas reciente.
    '''

    print('{}% Extrayendo la tabla de misiones.'.format(int(0/8*100)))
    misiones_0 = cplanimport(mode_0)

    dia_de_plan = input('{}% Introducir BatchID: '.format(int(1/8*100)))
    Date_Code_BatchID = int(dia_de_plan)

    cplanxgen2(misiones_0, Date_Code_BatchID)

    return Date_Code_BatchID

def generar_archivos(mode_0):
    '''
    Funcion de gestion de generacion del OK, SETPARAs Y RECEIVETASKs. Asi mismo dispara la creacion de los directorios de alojamiento de los archivos.
    '''

    key0 = 'plans'
    key1 = 'missions'
    rootes = routing(mode_0)
    container = rootes[key0]
    location = rootes[key1]
    print(container, location)

    procexgen2(container, location)

def actualiza_DB(mode_0):
    '''
    Funcion de gestion la actualizacion de la tabla de control de procesos.
    '''
    
    key = 'database'
    mode = False
    directorio = routing(mode)[key]
    S_base_datos = directorio + 'vrss_operation_and_managment_subsystem'
    S_tabla = '`control_misiones_id_control_process`'


    key = 'plans'
    container = routing(mode_0)[key]

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