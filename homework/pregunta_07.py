"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    df_sumaC2_por_letraC1_tbl0 = pd.read_csv("files/input/tbl0.tsv", delimiter="\t") #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_sumaC2_por_letraC1_tbl0'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_sumaC2_por_letraC1_tbl0.groupby("c1")["c2"].sum()     #? Agrupar los datos por la columna 'c1' (letras) y calcular la suma de la columna 'c2' para cada grupo. 'groupby("c1")' agrupa los datos por las letras de la columna 'c1', y '.sum()' calcula la suma de los valores de 'c2' para cada letra