from V2Gen.extractID import IDUpdate


def ID_Update():

    dia_de_plan = input('{}% Introducir BatchID: '.format(int(0/8*100)))

    Date_Code_BatchID = int(dia_de_plan)

    print('{}% Actualizando registro de control de procesos.'.format(int(8/8*100)))
    df = IDUpdate(Date_Code_BatchID)

    print(df)