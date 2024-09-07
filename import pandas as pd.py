import pandas as pd

# Crear un DataFrame simple
data = {
    'Nombre': ['Ana', 'Luis', 'Pedro'],
    'Edad': [23, 29, 35]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Acceder a una columna
print("Columna de edades:\n", df['Edad'])

# Filtrar filas con edades mayores a 25
filtro_edades = df[df['Edad'] > 25]
print("Filas con edad > 25:\n", filtro_edades)
