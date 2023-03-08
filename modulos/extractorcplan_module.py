
import pandas as pd
from datetime import datetime

def extractorcplan():
    '''
    ABAE-SAT-UT-SGO
    Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
    Creación: 2022-08-25
    Actualización: 2022-08-25
      Script para extraccion del plan de misiones con exportacion
      a *.csv.
    '''

    archivo_0 = input('Introduzca ruta del archivo: ')

    tiempo = datetime.strftime(
        datetime.now()
        , '%Y%m%d%H%M%S'
    )

    misiones_0 = pd.read_excel(archivo_0, sheet_name='Progresion de Accesos')

    cabeceras = {}
    cabeceras[misiones_0.columns[32]] = 'HRC/IRC (Teorico)'

    misiones_0 = misiones_0.rename(
        columns = cabeceras
    )

    return misiones_0