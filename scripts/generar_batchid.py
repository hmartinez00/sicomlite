from modulos.cplanxgen2_module import cplanxgen2
from modulos.procexgen2_module import procexgen2
from modulos.IDUpdate_module import ID_Update
from modulos.cplanimport_module import cplanimport


print('{}% Extrayendo la tabla de misiones.'.format(int(0/8*100)))
misiones_0 = cplanimport()

dia_de_plan = input('{}% Introducir BatchID: '.format(int(1/8*100)))
Date_Code_BatchID = int(dia_de_plan)

cplanxgen2(misiones_0, Date_Code_BatchID)
procexgen2()

pregunta = input('Desea actualizar la tabla de procesos? (S/N): ')

if pregunta == 's' or pregunta == 'S':
    try:
        ID_Update(Date_Code_BatchID)
    except:
        print('Directorio No encontrado!')

else:
    pass