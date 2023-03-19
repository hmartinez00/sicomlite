from modulos.processes.cplanxgen2_module import cplanxgen2
from modulos.builders.cplanimport_module import cplanimport


def generar_CPLAN():

    print('{}% Extrayendo la tabla de misiones.'.format(int(0/8*100)))
    mode = False
    misiones_0 = cplanimport(mode)

    dia_de_plan = input('{}% Introducir BatchID: '.format(int(1/8*100)))
    Date_Code_BatchID = int(dia_de_plan)

    cplanxgen2(misiones_0, Date_Code_BatchID, mode)