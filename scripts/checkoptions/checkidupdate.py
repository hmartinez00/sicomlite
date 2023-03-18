from ManageDB.sqlite_on_db import selectall
from modulos.processes.routing_module import routing


key = 'database'
mode = False
base_datos = routing(mode)[key] + 'vrss_operation_and_managment_subsystem'
tabla = '`control_misiones_id_control_process`'
sqlitedf = selectall(base_datos, tabla)
print(sqlitedf)