"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    df_tablaC1_listaC2 = pd.read_csv("files/input/tbl0.tsv", delimiter="\t")     #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_count_c2'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_tablaC1_listaC2.groupby("c1")[["c2"]].agg(func = lambda s: ":".join(sorted(s.map(str))))  #? Agrupar los datos por la columna 'c1' y para cada grupo de 'c1', aplicar una función que:
    #?  Toma la columna 'c2'.
    #?  Convierte los valores de la columna 'c2' a cadenas de texto con 'map(str)'.
    #?  Ordena los valores de 'c2' de forma ascendente con 'sorted()'.
    #?  Une los valores ordenados con ':' como separador utilizando ':'.join()