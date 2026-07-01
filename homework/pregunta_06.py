"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df_valorUnicoC4_tbl1_CapitalSorted = pd.read_csv("files/input/tbl1.tsv", delimiter="\t")   #? Leer el archivo `tbl1.tsv` y cargarlo en un DataFrame llamado 'df_valorUnicoC4_tbl1_CapitalSorted'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_valorUnicoC4_tbl1_CapitalSorted["c4"].str.upper().sort_values().unique().tolist() #? 
    #? Seleccionar la columna 'c4', convertir los valores a mayúsculas con `.str.upper()`, 
    #? ordenar alfabéticamente con `.sort_values()`, obtener los valores únicos con `.unique()`, 