


# * Ejercicio 1

import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd

ventas_empresa = {
    "Ventas Año 2020" : [20, 30 ,40, 50, 60, 90, 40, 30, 10, 30, 10, 30],
    "Ventas Año 2021": [25, 35, 30, 45, 55, 80, 50, 35, 20, 40, 15, 35],
    "Ventas Año 2022": [30, 40, 50, 60, 70, 95, 60, 40, 25, 45, 20, 50],
    "Ventas Año 2023": [35, 30, 45, 55, 65, 85, 55, 30, 30, 50, 25, 40],
    "Ventas Año 2024": [40, 50, 60, 70, 80, 110, 75, 50, 35, 60, 30, 65],
    "Ventas Año 2025": [45, 55, 50, 65, 85, 100, 70, 45, 40, 55, 35, 70],
    "meses" : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
}



usuario_fecha = int(input("¿De que año quieres ver las ventas? "))
columna_año = f"Ventas Año {usuario_fecha}"

df = pd.DataFrame(ventas_empresa)


tabla = plt.plot(df['meses'], df[columna_año])

plt.title(f"Ventas del año {usuario_fecha}")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



# * Ejercicio 2

import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd

notas_curso = {
    "Mates" : [8, 7, 9, 8, 9],
    "Lengua" : [7, 9, 7, 8, 6],
    "Geografia" : [8, 7, 6,8, 9],
    "Alumnas" : ['Mireya', 'Isa', 'Elena Diaz', 'Paloma', 'Victoria']
}


df = pd.DataFrame(notas_curso)

df['media_notas'] = (df["Mates"] + df["Lengua"] + df["Geografia"]) / 3


plt.bar(df['Alumnas'], df['media_notas'])
plt.title("Las mejores alumnas")
plt.show()

# * Ejercicio 3

import pandas as pd
import matplotlib.pyplot as plt

notas_alumnos = {
    "Materias" : ['Matematica', 'Lengua', 'Geografia'],
    "Alumnos" : ['Mireya', 'Elena Diaz', 'Isa'],
    'Notas' : [7,9,2],
}


df = pd.DataFrame(notas_alumnos)

df.plot.box(x= 'Alumnos', y= 'Notas')
plt.title("Distribución de notas")
plt.show()


# * Ejercicio 4


import pandas as pd
import matplotlib.pyplot as plt


ventas_años_2021 = {
    'Meses' : ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    'Ventas' : [24500, 18200, 31000, 28400, 35600, 42100, 45000, 39800, 27300, 22100, 33500, 48900]
}

df = pd.DataFrame(ventas_años_2021)

plt.pie( df['Ventas'], labels=df['Meses'], startangle= 90)
plt.title("Un titulo")
# plt.savefig()
plt.show()


# * Ejercicio 5

import pandas as pd
import matplotlib.pyplot as plt


ventas_empresa = {
    "Ventas Año 2020" : [20, 30 ,40, 50, 60, 90, 40, 30, 10, 30, 10, 30],
    "Ventas Año 2021": [25, 35, 30, 45, 55, 80, 50, 35, 20, 40, 15, 35],
    "Ventas Año 2022": [30, 40, 50, 60, 70, 95, 60, 40, 25, 45, 20, 50],
    "Ventas Año 2023": [35, 30, 45, 55, 65, 85, 55, 30, 30, 50, 25, 40],
    "Ventas Año 2024": [40, 50, 60, 70, 80, 110, 75, 50, 35, 60, 30, 65],
    "Ventas Año 2025": [45, 55, 50, 65, 85, 100, 70, 45, 40, 55, 35, 70],
    "meses" : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
}

df = pd.DataFrame(ventas_empresa)

# # 1 Gráfica de líneas
# df.plot.line()
# # 1 Gráfica de barras
# df.plot.bar()
# # 1 Gráfica circular
# df.set_index('meses', inplace=True)
# df['Ventas Año 2020'].plot.pie(autopct='%1.1f%%')
# # 1 Grafica de areas
# df.plot.area()

plt.title("Número de ventas")
plt.show()

# * Ejercicio 6


import pandas as pd
import matplotlib.pyplot as plt

ventas_empresa = {
    "Ingresos" : [20, 30 ,40, 50, 60, 90, 40, 30, 10, 30, 10, 30],
    "Gastos": [25, 35, 30, 45, 55, 80, 50, 35, 20, 40, 15, 35],
    "meses" : ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
}



df = pd.DataFrame(ventas_empresa).set_index('meses')

df.plot.line()
plt.xlabel("Meses")
plt.ylabel("cantidad Gastos/Ingresos")
plt.ylim(bottom=0)
plt.show()


# * Ejercicio 7

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Bloque_5/ejercicio_opcional_tema_5/bancos.csv")


print("Selecciona el rango de ventas")
nombre_banco_elegido = int(input("Dime el banco que deseas ver la cotización 1 -> Santander; 2 -> Sabadell; 3 -> Bankinter; 4 -> BBVA; 5 -> CaizaBank: "))
nombre_banco = ""

match nombre_banco_elegido:
    case 1:
        nombre_banco = "Banco Santander"
    case 2:
        nombre_banco = "Banco Sabadell"
    case 3: 
        nombre_banco = "Bankinter"
    case 4:
        nombre_banco = "BBVA"
    case 5:
        nombre_banco = "Caixabank"



filtrar_nombre_banco = df.loc[df["Empresa"] == nombre_banco] 



plt.plot(filtrar_nombre_banco['Fecha'], filtrar_nombre_banco['Cierre'])
plt.show()


santander = df.loc[df["Empresa"] == "Banco Santander"] 
bbva = df.loc[df["Empresa"] == "BBVA"] 
bankinter = df.loc[df["Empresa"] == "Bankinter"] 
sabadell = df.loc[df["Empresa"] == "Banco Sabadell"] 
caixabank = df.loc[df["Empresa"] == "Caixabank"] 

plt.plot(santander['Fecha'], santander['Cierre'])
plt.plot(bbva['Fecha'], bbva['Cierre'])
plt.plot(bankinter['Fecha'], bankinter['Cierre'])
plt.plot(sabadell['Fecha'], sabadell['Cierre'])
plt.plot(caixabank['Fecha'], caixabank['Cierre'])
plt.show()





# * Ejercicio 8

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Bloque_5/ejercicio_opcional_tema_5/titanic.csv").set_index('PassengerId')

# 1 Diagrama de fallecidos y superviviembtes

numero_supervivientes = sum(df['Survived'] == 1)
numero_fallecidos = sum(df['Survived'] == 0)

datos_graficos = pd.Series(data=[numero_supervivientes, numero_fallecidos], index=['Supervivientes' , 'Fallecidos'])

datos_graficos.plot.pie(autopct='%1.1f%%')


plt.title("Supervivientes titanic")
plt.show()


# 2 Histograma con  las edades

df['Age'].plot.hist(bins= 15)
plt.show()

# 3 Diagrama de Barras con el número de personas en cada clase

clase_1 = sum(df['Pclass'] == 1)
clase_2 = sum(df['Pclass'] == 2)
clase_3 = sum(df['Pclass'] == 3)

datos_grafico_clase = pd.Series(data=[clase_1, clase_2, clase_3], index=['Clase 1', 'Clase 2', 'Clase 3'])

datos_grafico_clase.plot.bar()
plt.show()


# 4 Diagrama de barras con el numero de personas fallecidas y supervivvientes en cada clase

clase_1_supervivientes = sum((df['Pclass'] == 1) & (df['Survived'] == 1))
clase_1_fallecidas = sum((df['Pclass'] == 1) & (df['Survived'] == 0))
clase_2_supervivientes = sum((df['Pclass'] == 2) & (df['Survived'] == 1))
clase_2_fallecidas = sum((df['Pclass'] == 2) & (df['Survived'] == 0))
clase_3_supervivientes = sum((df['Pclass'] == 3) & (df['Survived'] == 1))
clase_3_fallecidas = sum((df['Pclass'] == 3) & (df['Survived'] == 0))


datos_grafico_clase_supervivencia = pd.Series(data=[clase_1_supervivientes, clase_1_fallecidas, clase_2_supervivientes, clase_2_fallecidas, clase_3_supervivientes, clase_3_fallecidas], index=['Clase 1 Superviviente', 'Clase 1 Fallecidos', 'Clase 2 Superviviente', 'Clase 2 Fallecidos','Clase 3 Superviviente','Clase 3 Fallecidos'])

datos_grafico_clase_supervivencia.plot.barh()
plt.show()




# 5 Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase

datos_graficos = pd.crosstab(df['Survived'], df['Pclass'])


datos_graficos.plot.bar(
    stacked = True,
    color= ['#e57373', '#81c784']
)



plt.show()











