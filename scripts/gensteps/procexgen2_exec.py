from modulos.processes.procexgen2_module import procexgen2
from General_Utilities.control_rutas import setting_routes


key = 'resources'
container = setting_routes(key)[1]
procexgen2(container)