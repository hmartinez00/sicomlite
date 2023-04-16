import json
from ManageDB.sqlite_on_db import *
from General_Utilities.fecha import format_FechaID
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes
from MessagesKit.str_msg_format import buildmessage as bm
from modules.msgo_creator_module import msgo_sender, general_msgo_sender

database = r"2tim4_1.db"
Fecha = input('Introduzca la fecha: ')
Fecha = format_FechaID(Fecha)

key = 'tables'
tables = setting_routes(key)
option = option_list(tables)

if option != 'settings/tables/plan_biblia_52.json':
    msgo_sender(database, option, Fecha)
else:
    table = str(option).split('/')[-1].split('.')[0]
    List = [
        'Lectura',
        'Titulo',
        'Intro',
        'Encuesta'
    ]
    general_msgo_sender(database, table, Fecha, List)