from ManageDB.sqlite_on_db import selectall
from General_Utilities.control_rutas import setting_routes


key = 'databases'
base_datos = setting_routes(key)[0] + 'vrss_operation_and_managment_subsystem'
tabla = '`control_misiones_id_control_process`'
sqlitedf = selectall(base_datos, tabla)
print(sqlitedf)