import pandas as pd
import numpy as pd

diccionario_python={
    "Analisis":10,
    "Calificaciones":20,
    "Matematicas":30,
    "Derecho":40,
    "Español":50,
}
edades_diccionario=pd.Series(diccionario_python)

edades_diccionario

edades_diccionario.values

edades_diccionario.index

nuevos_indices = ['A', 'B', 'C', 'D', 'E']
arreglo_numpy =  ([10, 20, 30, 40, 50])
edades_diccionario = pd.series (arreglo_numpy, index =nuevos_indices)
edades_diccionario

edades_diccionario.dtypes

edades_diccionario.info()
