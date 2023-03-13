from modulos.IDUpdate_module import ID_Update


dia_de_plan = input('{}% Introducir BatchID: '.format(int(0/8*100)))

Date_Code_BatchID = int(dia_de_plan)

try:
    df = ID_Update(Date_Code_BatchID)
    print(df)
except:
    print('Directorio No encontrado!')