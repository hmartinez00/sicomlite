from modulos.processes.procexgen2_module import procexgen2
from modulos.processes.routing_module import routing


def generar_archivos():

    key = 'plans'
    mode = False
    container = routing(mode)[key]
    procexgen2(container, mode)