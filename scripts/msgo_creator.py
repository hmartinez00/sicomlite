from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import format_FechaID
from modulos.msgservice.msgo_creator_module import general_msgo_sender
from modulos.processes.routing_module import routing


key = 'database'
mode = False
database = routing(mode)[key] + 'vrss_operation_and_managment_subsystem'
Fecha = input('Introduzca la fecha: ')
Fecha = format_FechaID(Fecha)

# key = 'tables'
# tables = setting_routes(key)
# table = option_list(tables)
table = 'guardias'

# print(table)

List = [
    'Id',
    'planificador',
    'Apoyo',
    'dia_planificacion'
]

general_msgo_sender(database, table, Fecha, List)