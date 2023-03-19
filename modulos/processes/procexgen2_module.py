# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
from datetime import datetime
from V2Gen.procexmodule2 import *
from modulos.builders.trackingplan_module import trackingplan


def procexgen2(container, location):

    # ---------------------------------------------------------------------
    # Seleccionando el CPLAN
    #
    # Se selecciona el primer archivo con la extension CPLAN en el 
    # directorio.
    # ---------------------------------------------------------------------
    archivos = []
    for i in os.listdir(os.getcwd()):
        if '.CPLAN2' in i:
            archivos.append(i)

    archivo = archivos[0]

    fecha_hora = datetime.strptime(
        secuencia(CPLAN_extract(archivo))['TransStartTime'][0]
        , '%Y-%m-%dT%H:%M:%S'
    )

    # ---------------------------------------------------------------------
    # Extrayendo la información del plan de traqueo
    # ---------------------------------------------------------------------
    RecPass = trackingplan(location)
    RecPass['Diff'] = fecha_hora - RecPass['CaptureStartTime']
    CaptureTime_dict = near_orbits(CPLAN_extract(archivo), RecPass)

    # ---------------------------------------------------------------------
    # Creando árbol de directorios
    # ---------------------------------------------------------------------
    print('{}% Creando arbol de directorios.'.format(int(4/8*100)))
    directories_generator(directories_builder(CPLAN_extract(archivo), container))

    # ---------------------------------------------------------------------
    # Creando archivos de parámetros de cámara
    # ---------------------------------------------------------------------
    print('{}% Creando archivos de parametros de camara.'.format(int(5/8*100)))
    SETPARA_dict = SETPARAS_builder(CPLAN_extract(archivo))
    for ParameterFileCount in range(len(SETPARA_dict['MessageID'])):
        XML_SETPARA_Generator(SETPARA_dict, ParameterFileCount)
        
    # ---------------------------------------------------------------------
    # Creando certificado de envío
    # ---------------------------------------------------------------------
    print('{}% Creando certificado de envio.'.format(int(6/8*100)))
    XML_OK_generator(OK_builder(CPLAN_extract(archivo)))

    # ---------------------------------------------------------------------
    # Creando Tareas de recepción
    # ---------------------------------------------------------------------
    print('{}% Creando Tareas de recepcion.'.format(int(7/8*100)))
    RECEIVETASK_dict = RECEIVETASK_builder(CPLAN_extract(archivo), RecPass)
    for ParameterFileCount in range(len(RECEIVETASK_dict['MessageID'])):
        XML_RECEIVETASK_Generator(RECEIVETASK_dict, ParameterFileCount)
        
    # ---------------------------------------------------------------------
    # Organizando los archivos
    # ---------------------------------------------------------------------
    print('{}% Organizando archivos.'.format(int(8/8*100)))
    files_organizer(CPLAN_extract(archivo), RecPass, container)