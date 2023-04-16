import json
from ManageDB.sqlite_on_db import *
from General_Utilities.control_rutas import setting_routes
from modulos.msgservice.str_msg_format import build_Tmsg as btm


def general_msgo_sender(database, table, Fecha, List):

    # Definimos los source files
    key = 'sender'
    ruta_sender_json = setting_routes(key)[0]
    print(table)

    # Extraemos los datos de validacion requeridos del json
    with open(ruta_sender_json) as archivo_json:
        datos_json = json.load(archivo_json)

    url = datos_json['telegram']['TELEGRAM_URL']
    chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
    token = datos_json['telegram']['TELEGRAM_TOKEN']

    btm(
        database,
        table,
        Fecha,
        url,
        chat_id,
        token,
    ).sender(List)