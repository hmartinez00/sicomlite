# ---------------------------------------------------------------------
# ABAE-SAT-UT-SGO
# Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
# Creación: 2022-08-25
# Actualización: 2022-08-25
#
#   Script para extraccion del plan de misiones con exportacion
#   a *.csv.
#
# ---------------------------------------------------------------------

import os
import pandas as pd
from datetime import datetime, timedelta

archivo_0 = input('Introduzca ruta relativa del archivo: ')
os.chdir('..')

tiempo = datetime.strftime(
    datetime.now()
    , '%Y%m%d%H%M%S'
)

respaldo = 'backup/PMS/GPT/' + tiempo + '.csv'

misiones_0 = pd.read_excel(archivo_0, sheet_name='Progresion de Accesos')

cabeceras = {}
cabeceras[misiones_0.columns[32]] = 'HRC/IRC (Teorico)'

misiones_0 = misiones_0.rename(
    columns = cabeceras
)

pregunta = input('Desea exportar la tabla de misiones a csv? (S/N): ')

if pregunta == 's' or pregunta == 'S':
    misiones_0.to_csv(respaldo, index=False)
    misiones_0 = pd.read_csv(respaldo)
    print(respaldo + '\n')
else:
    print('No se ha exportado la tabla!' + '\n')