from MessagesKit.msgo import tg_msgo
from ManageDB.sqlite_on_db import *


class strTmsgformat:

    def __init__(
        self,
        __table__,
        __date__,
        __Lista__,
    ):
        self.__table__ = __table__
        self.__date__ = __date__
        self.__Lista__ = __Lista__

    def msgtext(self):
        if self.__table__ == 'guardias':
            send_pasaje = \
            f"Saludos. Aca el proximo equipo de guardia de OMS designado para la semana del {self.__date__} (Semana Nro {self.__Lista__[0]}), acorde al cronograma de guardias:\n\n" + \
            f"Planificacion: {self.__Lista__[1]}\n" + \
            f"Personal de apoyo: {self.__Lista__[2]}."

        else:
            print('''Error en modulo str_msg_format.py:

            El formato de mensaje para las entradas de esta tabla no se ha anadido!''')

        return send_pasaje


class build_Tmsg:

    def __init__(
        self,
        __database__,
        __table__,
        __Fecha__,
        __url__,
        __chat_id__,
        __token__,
    ):

        self.__database__ = __database__
        self.__table__ = __table__
        self.__Fecha__ = __Fecha__
        self.__url__ = __url__
        self.__chat_id__ = __chat_id__
        self.__token__ = __token__

    def sender(self, __Lista__):
        
        N_lista = []

        # Extraemos los datos de la base de datos
        df = selectall(self.__database__, self.__table__)
        df = df[df['dia_planificacion'] == self.__Fecha__].reset_index()

        for i in range(len(__Lista__)):
            entry = df[__Lista__[i]].iloc[0]
            print(entry)
            N_lista.append(entry)

        # Construimos los mensajes
        send_pasaje = strTmsgformat(
                self.__table__,
                self.__Fecha__,
                N_lista
            ).msgtext()

        print(send_pasaje)

        # Enviamos los mensajes
        tg_msgo(
            self.__url__,
            self.__chat_id__,
            self.__token__,
            send_pasaje,
        ).telegram_sender()