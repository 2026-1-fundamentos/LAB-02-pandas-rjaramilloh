"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)
def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    cantidad_tbl0_tvs = pd.read_csv("files/input/tbl0.tsv", delimiter = "\t" )      #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'cantidad_tbl0_tvs'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return cantidad_tbl0_tvs.shape[1]                           #? Devolver la cantidad de columnas en el DataFrame. 'shape[1]' obtiene el número de columnas (el segundo valor de la tupla 'shape')