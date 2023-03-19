from modulos.exec.exec_module import generar_TCPLAN, generar_CPLAN, generar_archivos, actualiza_DB


mode = False
generar_TCPLAN(mode)

mode = False
Date_Code_BatchID = generar_CPLAN(mode)

print(Date_Code_BatchID)

mode = False
generar_archivos(mode)

mode = False
actualiza_DB(mode)