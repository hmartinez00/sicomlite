from ManageDB.mysql_on_db import mysql_extract_table_df
from ManageDB.sqlite_on_db import selectall


base_datos = 'vrss_operation_and_managment_subsystem'
tabla = '`control_misiones_id_control_process`'
# mqldf = mysql_extract_table_df(base_datos, tabla)
sqlitedf = selectall(base_datos, tabla)
# print(mqldf)
print(sqlitedf)