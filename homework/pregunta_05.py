"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    df_maxc2_por_letrac1_tbl10 =  pd.read_csv("files/input/tbl0.tsv", delimiter="\t")   #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_max_c2porc1_tbl0'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_maxc2_por_letrac1_tbl10.groupby("c1")["c2"].max()                         #? Agrupar los datos por la columna 'c1' (letras) y calcular el valor máximo de la columna 'c2' para cada grupo. 'groupby("c1")' agrupa los datos, y '.max()' calcula el valor máximo de 'c2' por cada letra de 'c1'