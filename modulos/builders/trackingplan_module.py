# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
import pandas as pd
from V2Gen.procexmodule2 import TCPLAN_extract
from modulos.processes.routing_module import routing


# ---------------------------------------------------------------------

def trackingplan(mode):

    '''
    ABAE-SAT-UT-SGO
    Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
    Creación: 2022-08-20
    Actualización: 2022-08-29
      Script para actualizacion del TCPLAN.
    '''

    # ---------------------------------------------------------------------
    # Recabando info de XMLs.
    # ---------------------------------------------------------------------
    if mode == True or mode == False:
        key = 'missions'
        directorio = routing(mode)[key]
    else:
        directorio = mode

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

    df[df.index.name] = [i for i in range(len(df))]
    df.set_index(df.index.name,inplace=True)
    df.index.name = None

    # df['CaptureEndTime'] = pd.to_datetime(df['CaptureEndTime'])
    # df['StartLocalTime'] = pd.to_datetime(df['StartLocalTime'])
    # df['EndLocalTime'] = pd.to_datetime(df['EndLocalTime'])
    # df['MadeTime'] = pd.to_datetime(df['MadeTime'])

    df0 = df.iloc[:,:4]
    df1 = df.iloc[:,4:].apply(pd.to_datetime, errors='coerce')

    df = pd.concat([df0, df1], axis=1)

    return df

    # ---------------------------------------------------------------------
