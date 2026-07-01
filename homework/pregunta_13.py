"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    tbl0 = pd.read_csv("files/input/tbl0.tsv", delimiter="\t") #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'tbl0'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    tbl2 = pd.read_csv("files/input/tbl2.tsv", delimiter="\t") #? lo mismo pero con "tbl2.tvs"
    
    return tbl0.merge(tbl2, on="c0").groupby("c1")["c5b"].sum() #? 
    #? Hacer una fusión de los DataFrames 'tbl0' y 'tbl2' usando la columna 'c0' como clave con 'merge(on="c0")'.
    #? Luego, agrupar los datos resultantes por la columna 'c1' y calcular la suma de los valores de la columna 'c5b' para cada grupo con '.groupby("c1")["c5b"].sum()'.