from ManageDB.sqlite_on_db import selectall


base_datos = 'vrss_operation_and_managment_subsystem'
tabla = '`control_misiones_id_control_process`'
sqlitedf = selectall(base_datos, tabla)
print(sqlitedf)