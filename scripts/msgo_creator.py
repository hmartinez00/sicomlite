from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import format_FechaID
from modulos.msgservice.msgo_creator_module import general_msgo_sender
from modulos.processes.routing_module import routing
from General_Utilities.fecha import format_FechaID, DeltaT


key = 'database'
mode = False
database = routing(mode)[key] + 'vrss_operation_and_managment_subsystem'
# key = 'tables'
# tables = setting_routes(key)
# table = option_list(tables)
table = 'guardias'

fecha = input('Introduzca la fecha: ')
ahora = format_FechaID(fecha)

for i in range(4):
    j = 7 * i
    print(DeltaT(ahora, -j))
    Fecha = DeltaT(ahora, -j)

    List = [
        'Id',
        'planificador',
        'Apoyo',
        'dia_planificacion'
    ]

    general_msgo_sender(database, table, Fecha, List)