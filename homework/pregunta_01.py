"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)
def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    cantidad = pd.read_csv("files/input/tbl0.tsv")      #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'cantidad'.
    return cantidad.shape[0]                            #? Devolver la cantidad de filas en el DataFrame. 'shape[0]' obtiene el número de filas (el primer valor de la tupla 'shape')