from modulos.exec.exec_module import generar_TCPLAN, generar_CPLAN, generar_archivos, actualiza_DB


mode = True
Date_Code_BatchID = generar_CPLAN(mode)

print(Date_Code_BatchID)