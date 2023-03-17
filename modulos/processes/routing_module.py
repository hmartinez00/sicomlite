import os
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


def routing(clave = None):
    key = 'resources'
    directorio = setting_routes(key)[0]

    folders = os.listdir(directorio)
    compendium = directorio + option_list(folders[2:])

    enrutamiento = {}

    enrutamiento['database'] = directorio + 'data/'
    enrutamiento['compendium'] = compendium
    enrutamiento['missions'] = compendium + '/Seleccion de Misiones/'
    enrutamiento['plans'] = compendium + '/Planes Satelitales/'

    if clave != None:
        res = [enrutamiento, enrutamiento[clave]]
    else:
        res = [enrutamiento]

    return res