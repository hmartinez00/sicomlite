from V2Gen.extractID import IDUpdate


def ID_Update(Date_Code_BatchID):

    print('{}% Actualizando registro de control de procesos.'.format(int(8/8*100)))
    df = IDUpdate(Date_Code_BatchID)

    return df