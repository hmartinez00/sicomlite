from modulos.exec.exec_tcplanprepare import generar_TCPLAN
from modulos.exec.exec_cplanxgen2 import generar_CPLAN
from modulos.exec.exec_procexgen2 import generar_archivos
from modulos.exec.exec_idupdate import actualiza_DB


generar_TCPLAN()
generar_CPLAN()
generar_archivos()
actualiza_DB()