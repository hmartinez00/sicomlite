# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import os
from datetime import datetime
from V2Gen.procexmodule2 import *
from modulos.trackingplan_module import trackingplan


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

print(archivo)

fecha_hora = datetime.strptime(
     secuencia(CPLAN_extract(archivo))['TransStartTime'][0]
     , '%Y-%m-%dT%H:%M:%S'
)

# ---------------------------------------------------------------------
# Extrayendo la información del plan de traqueo
# ---------------------------------------------------------------------
RecPass = trackingplan()
RecPass['Diff'] = fecha_hora - RecPass['CaptureStartTime']
CaptureTime_dict = near_orbits(CPLAN_extract(archivo), RecPass)

print(RecPass)