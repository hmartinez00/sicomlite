# ---------------------------------------------------------------------
# Importamos las librerías.
# ---------------------------------------------------------------------
import pandas as pd
from modulos.builders.extractorcplan_module import extractorcplan


def cplanimport(mode):
    '''
    ABAE-SAT-UT-SGO
    Desarrollado por: Héctor Martínez (Jefe(E) Telecomunicaciones)
    Creación: 2022-08-20
    Actualización: 2022-08-20
          Script para actualizacion del TCPLAN.
    '''

    # ---------------------------------------------------------------------
    # Levantando el Dataframe General.

    # Este segmento organiza en un  Dataframe toda la informacion
    # que se encuentra almacenada en los archivos CSV del directorio
    # GPT (General Plan table).
    # ---------------------------------------------------------------------
    misiones_0 = extractorcplan(mode)
    misiones_0['Date'] = pd.to_datetime(misiones_0['Date'])


    # ---------------------------------------------------------------------
    # Filtrando las misiones seleccionas
    # ---------------------------------------------------------------------
    misiones_0 = misiones_0[misiones_0['Index'] >= 10]
    misiones_0[misiones_0.index.name] = [i for i in range(len(misiones_0))]
    misiones_0.set_index(misiones_0.index.name,inplace=True)
    misiones_0.index.name = None

    Lista_columnas_0 = misiones_0.columns

    Lista_columnas = []
    for i in misiones_0.columns:
        Lista_columnas.append(i\
                    .replace(' ', '_')\
                    .replace('(', '')\
                    .replace(')', '')\
                    .replace('ó', 'o')\
                    .replace('/', '_')\
                    .replace('Index', 'Indice')\
                    .replace('-', '_')
            )

    diccionario = {}

    for i in range(len(Lista_columnas_0)):
        diccionario[Lista_columnas_0[i]] = Lista_columnas[i]

    df = misiones_0.rename(
        columns = diccionario
    )

    print(
            [
                df['Start_Time_UTCG'].min(),
                df['Start_Time_UTCG'].max()
            ]
        )

    return df
    # ---------------------------------------------------------------------
