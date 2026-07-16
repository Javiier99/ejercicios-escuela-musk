
# import json

# with open("Bloque_5/tema_2/archivojson.json" , "r") as file:
#     hola = json.load(file)


# print(f'Nuestra querida {hola["persona"][0]["name"]} y {hola["persona"][1]["name"]} tiene {hola["persona"][0]["edad"]} y {hola["persona"][1]["edad"]} añitos y sus trabajos es: {hola["persona"][1]["oficio"]}')


# persona = {
#     "name" : "Isa",
#     "edad" : 25,
#     "oficio": "Maestra"
# }

# hola["persona"].append(persona)


# with open("Bloque_5/tema_2/archivojson.json" , "w") as file:
#     json.dump(hola, file, indent=4)


# with open("Bloque_5/tema_2/archivojson.json" , "r") as file:
#     hola = json.load(file)


# print(f'Ahora se ha añadido una nueva chica llamada {hola["persona"][2]["name"]} que tiene {hola["persona"][2]["edad"]} añitos y sus trabajos es: {hola["persona"][2]["oficio"]} ')





# from datetime import datetime

# import datetime


# import pandas as pd





# import pandas as pd

# # 1. Crear un DataFrame desde cero (usando un diccionario)
# datos = {
#     'Producto': ['Teclado', 'Ratón', 'Monitor', 'Teclado', 'Auriculares'],
#     'Precio': [25.50, 15.00, 149.99, 25.50, 30.00],
#     'Cantidad': [2, 5, 1, 3, 2],
#     'Tienda': ['Norte', 'Sur', 'Norte', 'Este', 'Sur']
# }

# df = pd.DataFrame(datos)

# print("--- DataFrame Original ---")
# print(df)
# print("\n" + "a"*30 + "\n")

# # 2. Agregar una nueva columna calculada
# # Multiplicamos el precio por la cantidad para obtener el total de la venta
# df['Total'] = df['Precio'] * df['Cantidad']
# df['Dividido'] = df['Precio'] / df['Cantidad']

# print(df)

# # 3. Filtrar datos
# # Queremos ver solo las ventas que se hicieron en la tienda 'Sur'
# ventas_sur = df[df['Tienda'] == 'Sur']

# print("--- Ventas en la Tienda Sur ---")
# print(ventas_sur)
# print("\n" + "-"*30 + "\n")

# # 4. Agrupar y Analizar
# # Queremos saber cuánto se ha vendido en TOTAL por cada producto
# ventas_por_producto = df.groupby('Producto')['Total'].sum().reset_index()

# print("--- Total de Ventas por Producto ---")
# print(ventas_por_producto)






# import pandas as pd



# objetos = {
#     "Nombre" : ['Elena Díaz' , 'Mireya', 'Isa', 'Victoria', 'Paloma'],
#     "Edad" : [26,25,25,26,26],
#     "Oficio": ['Profe']*5,
#     "Años Cotizados" : [20, 20, 20, 18, 17]
# }

# df = pd.DataFrame(objetos)

# print(df)

# df['Nueva_Edad'] = df['Edad'] + 10

# print(df)


# df['Proximo Oficio'] = 'Bailarina'

# print(df)


# edad_26 = len(df[(df['Edad'] == 26) & (df['Años Cotizados'] < 20)])

# print(edad_26)

# df = df.drop(columns=['Edad'])

# print(df)


# lol = df.loc[:,['Nombre', 'Edad','Oficio']]
# print(lol)


# df['Van al trabajo'] = 'Si'
# df['Comen la comida en el almuerzo'] = df['Van al trabajo']
# print(df)


# df.loc[(df['Edad'] == 26), 'Cumpliran 27 este año'] = 'Si'
# df.loc[(df['Edad'] == 25), 'Cumpliran 27 este año'] = 'No'

# print(df)











# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# # 1. Creamos un DataFrame con datos de ejemplo
# datos = {
#     'Horas_Estudio': [10, 2, 8, 4, 15, 6, 12, 1, 7, 11],
#     'Asistencia_%':  [95, 40, 80, 60, 100, 75, 90, 20, 85, 92],
#     'Horas_Videojuegos': [1, 12, 3, 8, 0, 5, 2, 15, 4, 2],
#     'Nota_Final':    [9.0, 3.5, 7.5, 5.0, 10.0, 6.2, 8.8, 2.0, 7.0, 8.5]
# }

# df = pd.DataFrame(datos)

# # 2. Calculamos la matriz de correlación (valores entre -1 y 1)
# # numeric_only=True asegura que solo use columnas con números
# matriz_corr = df.corr(numeric_only=True)

# # 3. Configuramos el lienzo de Matplotlib
# fig, ax = plt.subplots(figsize=(8, 6))

# # 4. Dibujamos el Mapa de Calor con Seaborn
# sns.heatmap(
#     matriz_corr,           # Los datos de la matriz
#     annot=True,            # True: Muestra los números dentro de cada cuadro
#     cmap='coolwarm',       # Paleta de colores (Azul=Negativo, Rojo=Positivo)
#     fmt=".2f",             # Muestra los números con 2 decimales
#     linewidths=0.8,        # Separación física entre los cuadros
#     vmin=-1, vmax=1,       # Forzar a que la escala vaya de -1 a 1
#     ax=ax                  # Dibujarlo en el lienzo que creamos
# )

# # 5. Tuneamos los títulos con Matplotlib
# ax.set_title("Matriz de Correlación: Rendimiento Estudiantil", fontsize=14, fontweight='bold', pad=15)

# # 6. Guardamos la gráfica en alta calidad antes de mostrarla
# plt.savefig('heatmap_estudiantes.png', dpi=300, bbox_inches='tight')

# # 7. Mostramos la gráfica en pantalla
# plt.show()






# import pandas as pd

# datos = {
#     'nombre': ['Sirius', 'Vega', 'Betelgeuse'],
#     'edad': [25, 30, 35],
#     'ciudad': ['Orion', 'Lyra', 'Orion']
# }

# df = pd.DataFrame(data = datos) 

# fila1 = df.iloc[0]
# print(fila1)











# import numpy as np

# hola = np.empty(10)

# print(hola)




# import numpy as np
# a = np.array([1,20,13,4,2,200,42,3])
# b = np.array([6,5,3,9,6,45,554,435])

# print(a)
# print(b)
# hola = a*b
# print
# print(hola[2])




import matplotlib.pyplot as plt


import numpy as np

xpoints = np.array([0,89,90])
ypoints = np.array([0,2,250])

plt.plot(xpoints, ypoints)
plt.show()

