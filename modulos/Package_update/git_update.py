import os
from Pku_module.Package_update_module import auto_commit
from General_Utilities.option_list import option_list
from Pku_module.Package_update_module import listar_paquetes

os.chdir('..')
opciones = os.listdir()
project = option_list(opciones)

# print(project)

auto_commit(project)