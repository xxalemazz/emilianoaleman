import pandas as pd
import numpy as pd

lista_python = [
        [10,20,30,40],
        [50,60,70,80],
        [90,100,110,120]
]

diccionarios_listas={
    "Nombre":["Ciro", "imelda","jose"],
    "edad":[22,32,15],
    "Area":["ti", "rh", "produccion"]
}
df=pd.DataFrame(diccionarios_listas)

df

filas = ['a','b','c']
columnas = ['I','II','III','IV']
df = pd.DataFrame(lista_python,
                    index=filas,colums=columnas)
df
