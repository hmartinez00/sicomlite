from modulos.processes.IDUpdate_module import ID_Update
from General_Utilities.control_rutas import setting_routes


key = 'resources'
container = setting_routes(key)[1]

dia_de_plan = input('{}% Introducir BatchID: '.format(int(0/8*100)))

Date_Code_BatchID = int(dia_de_plan)

df = ID_Update(Date_Code_BatchID, container)
print(df)