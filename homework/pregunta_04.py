"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd                                         #? Importar la librería pandas, que se utiliza para trabajar con datos en formato de tablas (DataFrames)

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    df_promedio_c2porc1_tbl0 = pd.read_csv("files/input/tbl0.tsv", delimiter="\t") #? Leer el archivo `tbl0.tsv` y cargarlo en un DataFrame llamado 'df_promedio_c2porc1_tbl0'. El parámetro 'delimiter="\t"' indica que los valores están separados por tabulaciones (TSV)
    return df_promedio_c2porc1_tbl0.groupby("c1")["c2"].mean()     #? Agrupar los datos por la columna 'c1' (letras) y calcular el promedio de la columna 'c2' para cada grupo. 'groupby("c1")' agrupa los datos, y '.mean()' calcula el promedio de los valores de 'c2' por cada letra de 'c1'