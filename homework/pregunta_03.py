"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    df_cantidad_tbl0_letracolumna_c1 = pd.read_csv("files/input/tbl0.tsv", delimiter = "\t" )   #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'cantidad_tbl0_letracolumna_c1'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)   
    return df_cantidad_tbl0_letracolumna_c1.groupby("c1")["c1"].count()                         #? Agrupar los datos por la columna 'c1' y contar cuántos registros hay por cada letra de esa columna. 'groupby("c1")' agrupa los datos, y '.count()' cuenta la cantidad de registros por grupo