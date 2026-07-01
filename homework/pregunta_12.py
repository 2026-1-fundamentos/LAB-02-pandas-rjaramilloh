"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    df_c0_listc5a_c5b_tbl2 = pd.read_csv("files/input/tbl2.tsv", delimiter="\t")      #? Leer el archivo `tbl2.tsv` y cargarlo en un DataFrame llamado 'df_c0_listc5a_c5b_tbl2'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    #? Crear una nueva columna llamada 'c5' que concatene los valores de las columnas 'c5a' y 'c5b' separados por ':' usando el operador `+`. Convertir los valores de 'c5b' a cadenas con '.apply(str)' para asegurarse de que se puedan concatenar.
    df_c0_listc5a_c5b_tbl2["c5"] = df_c0_listc5a_c5b_tbl2["c5a"] + ":" + df_c0_listc5a_c5b_tbl2["c5b"].apply(str) 
    
    return df_c0_listc5a_c5b_tbl2.groupby("c0", as_index = False)[["c5"]].agg(lambda s: ",".join(sorted(s)))
    #? Agrupar los datos por la columna 'c0', mantener 'c0' como una columna en lugar de índice con 'as_index=False', y para cada grupo de 'c0', aplicar una función que:
    #? Ordena los valores de la columna 'c5' de forma ascendente con 'sorted(s)'.
    #? Une los valores ordenados con una coma (`,`) como separador usando '",".join()'.