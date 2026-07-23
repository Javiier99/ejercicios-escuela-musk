

# ! Apunte: No me deja subir la carpeta con todos los archivos que se ha usado para hacer los ejercicios, se lo mando tal cual, si es necesario la carpeta, me podrías facilitar un metodo de envio? Un saludo


# ! Tema 1

# * Ejercicio 1

with open("ejercicios_obligatorio_tema_5/archivos_creados/poema.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i.strip())
    


# * Ejercicio 2

with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:
    lineas = file.readlines()
    numero_lineas = len(lineas)
    print(numero_lineas)



# * Ejercicio 3


with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:

    frases = file.readlines()

    contador = 0
    for i in frases:
        numero_palabras = len(i.split())
        contador += numero_palabras
    print(contador)


# * Ejercicio 4

with open("ejercicios_obligatorio_tema_5/archivos_creados/notas.txt", "r", encoding="utf-8") as file:
    contador_el = []
    num_contador_el = 0
    frase_entera = file.read()
    frase_dividida = frase_entera.split()
    contador = 0
    for i in range(len(frase_dividida)):
        palabras = frase_dividida[i]
        contador += 1
        if(palabras == "el") or (palabras == "El"):
            contador_el.append(contador)
            num_contador_el += 1
    
    print(f'Tenemos {num_contador_el} "el" y sus posiciones son {contador_el}')



# * Ejercicio 5

def display_words(texto_dividido):
    mostrar_palabras = []
    for i in range(len(texto_dividido)):
        contador_letras= len(texto_dividido[i])

        if(contador_letras < 4):
            mostrar_palabras.append(texto_dividido[i])

    return mostrar_palabras

with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:
    texto_dividido = file.read().split()
    resultado = display_words(texto_dividido)
    
    print(f"Palabras con menos de 4 caracteres: {resultado}")


# * Ejercicio 6


def hash_display(todo_texto, letra_especial):
    resultado_lista = []
    list_texto = todo_texto.split()
    for i in list_texto:
        guardar_texto = ""
        for x in range(len(i)):
            guardar_texto += i[x].join(f" {letra_especial}")
        sin_espacios = guardar_texto.replace(" ", "")
        resultado_lista.append(sin_espacios)
    texto = " ".join(resultado_lista)
    return texto


letra_especial = str(input("¿Qué letra especial quieres poner? "))

with open("ejercicios_obligatorio_tema_5/archivos_creados/materia.txt", "r", encoding="utf-8") as file:
    todo_texto = file.read().strip()
    resultado = hash_display(todo_texto, letra_especial)
    
    print(resultado)


# * Ejercicio 7


import string

for i in range(len(string.ascii_uppercase)):
    with open(f"ejercicios_obligatorio_tema_5/archivos_creados/generador_archivo_ejercicio_7/{string.ascii_uppercase[i]}.txt", "w", encoding="utf=8") as file:
        file.write(f"{string.ascii_uppercase[i]}")



# * Ejercicio 8

with open("ejercicios_obligatorio_tema_5/archivos_creados/python.txt", "a" , encoding="utf-8") as file:
    file.write("Cualquier texto")

with open("ejercicios_obligatorio_tema_5/archivos_creados/python.txt", "r" , encoding="utf-8") as file:
    print(file.read())



# * Ejercicio 9

with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt" , "r", encoding="utf-8") as file:
    texto_completo = file.read().split()
contador_palabras = []
for i in range(len(texto_completo)):
        palabra_contabilizada = False
        for x in range(len(contador_palabras)):
            if(contador_palabras[x][0].lower() == texto_completo[i].lower()):
                contador_palabras[x][1] += 1
                palabra_contabilizada = True
        
        if(palabra_contabilizada == False):
                contador_palabras.append([texto_completo[i].lower() ,1])


print(contador_palabras)


# * Ejercicio 10

from pathlib import Path


archivo_encontrados = list(Path(".").rglob("notas.txt"))

if(archivo_encontrados):
    for i in archivo_encontrados:
        print(f"El archivo existe, está {i}")

else:
    print("El archivo no existe")




# ! Tema 2

# * Ejercicio 1

import csv

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding="utf-8") as file:
    lineas = csv.reader(file)
    cabecera = next(lineas)
    contador_5_primeras_lineas = 0
    contador_5_ultimas_lineas = 0
    for i in lineas:
        print(i)
        contador_5_primeras_lineas += 1
        if(contador_5_primeras_lineas == 5):
            break
    lineas_listas = list(lineas)
    for i in reversed(lineas_listas):
        print(i)
        contador_5_ultimas_lineas += 1
        if(contador_5_ultimas_lineas == 5):
            break


# * Ejercicio 2

import csv

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding="utf-8") as file:
    archivo =  list(csv.DictReader(file))

# cabecera = next(archivo)

# 1 Dado que no hay ningún dato que sea Nan, crearé una columna nueva y lo pondré alli para posteriormente cambiarlo por otro dato 

for i in archivo:
    i['nueva_columna'] = None

cabecera = ['','index','company','body-style','wheel-base','length','engine-type','num-of-cylinders','horsepower','average-mileage','price','nueva_columna']

# 1 Escribimos una nueva columna
with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "w", newline='', encoding="utf-8") as file:
    escribir = csv.DictWriter(file, fieldnames=cabecera)
    escribir.writeheader()
    escribir.writerows(archivo)

# 1 Sustituimos la nueva el texto nan, por otro con un condicional

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", newline='', encoding="utf-8") as file:
    archivo_cambiado = list(csv.DictReader(file))

for i in archivo_cambiado:
    if(i['company'] == 'honda'):
        i['nueva_columna'] = "Esto es una sustitución"

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "w", newline='', encoding="utf-8") as file:
    escribir = csv.DictWriter(file, fieldnames=cabecera)
    escribir.writeheader()
    escribir.writerows(archivo_cambiado)


# * Ejercicio 3

import csv

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding='utf-8') as file:
    archivo_leido = list(csv.DictReader(file))

guardar_dato = {'Nombre Empresa' : '', 'Precio' : 0, 'Posición' : 0}
contador = 1 # Tenemos 1 ya que empezamos contando la cabecera
for i in archivo_leido:
    try:
        precio_csv = float(i['price'])
        if(precio_csv > guardar_dato['Precio']):
            guardar_dato['Nombre Empresa'] = i['company']
            guardar_dato['Precio'] = precio_csv
            guardar_dato['Posición'] = contador + 1 # le sumamos 1 ya que el contador está al final y no llega a contar y guardar la fila exacta donde se encuentra el vehículo más caro
            
        
        contador += 1
    except ValueError:
        contador += 1
        continue
    

print(f"La empresa con el coche más caro es {guardar_dato['Nombre Empresa']} y su precio es: {guardar_dato['Precio']}€ su posición es: {guardar_dato['Posición']}")



# * Ejercicio 4

import csv
with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
    archivo = list(csv.DictReader(file))


for i in archivo:
    if(i['company'] == 'toyota'):
        print(i)


# * Ejercicio 5

import csv
from collections import Counter

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
    archivo = list(csv.DictReader(file))

empresas = []
for i in archivo:
    empresas.append(i['company'])

conteo_empresas = Counter(empresas)

# * Ejercicio 6

import csv
from collections import Counter

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
    archivo = list(csv.DictReader(file))


guardar_marca_precio_altos = {}

for coches in archivo:
    empresa = coches['company']
    try:
        precio = float(coches['price'])
    except:
        precio = 0.0

    
    if ((empresa not in guardar_marca_precio_altos) or (precio > guardar_marca_precio_altos[empresa])):
        guardar_marca_precio_altos[empresa] = precio

print(guardar_marca_precio_altos)




# * Ejercicio 7

# 1 Comenta el ejercicio el kilometraje medio, pero no veo como tal en el csv, por lo que voy a usar consumo medio (average-mileage)

import csv

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding='utf-8') as file:
    archivo = list(csv.DictReader(file))

guardar_consumo_medio = {}

for i in archivo:
    empresa = i['company']
    try:
        consumo_medio = float(i['average-mileage'])
    except:
        consumo_medio = 0
    
    if(empresa not in guardar_consumo_medio):
        guardar_consumo_medio[empresa] = [consumo_medio]
    else:
        guardar_consumo_medio[empresa].append(consumo_medio)



for marca in guardar_consumo_medio.items():
    calculo_media = round(sum(marca[1]) / len(marca[1]) , 2)
    guardar_consumo_medio[marca[0]] = calculo_media
    

print(guardar_consumo_medio)




# * Ejercicio 8

import csv

with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding='utf-8') as file:
    archivo = list(csv.DictReader(file))



for i in range(len(archivo)):
    try:
        if(1 < float(archivo[i]['price'])):
            archivo[i]['price'] = float(archivo[i]['price'])
    except:
        archivo[i]['price'] = 0

parar = False
while parar == False:
    hay_cambio = False

    for i in range(len(archivo) - 1):
        if(archivo[i]['price'] < archivo[i + 1]['price']):
            archivo[i], archivo[i + 1] = archivo[i + 1], archivo[i]
            hay_cambio = True

    if(hay_cambio == False):
        parar = True


# 1 (Extra) Lo escribimos en un nuevo csv para que quede guardado los cambios
nombre_columnas = archivo[0].keys()

with open("ejercicios_obligatorio_tema_5/archivos_creados/precio_automovil_mayor_menor.csv", "w", encoding='utf-8', newline='') as file:
    escribir = csv.DictWriter(file, fieldnames=nombre_columnas)
    escribir.writeheader()
    escribir.writerows(archivo)


# * Ejercicio 9


GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
    'Price': [23845, 171995, 135925, 71400],
}
japaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
    'Price': [29995, 23600, 61500, 58900],
}

import pandas as pd

dataframe_GermanCars = pd.DataFrame(GermanCars)
dataframe_japaneseCars = pd.DataFrame(japaneseCars)


concatenado = pd.concat([dataframe_GermanCars, dataframe_japaneseCars], ignore_index=True)

print(concatenado)




# * Ejercicio 10


Car_Price = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'Price': [23845, 17995, 135925, 71400],
}
car_Horsepower = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'horsepower': [141, 80, 182, 160],
}

import pandas as pd

data_frame_price = pd.DataFrame(Car_Price)
data_frame_horsepower = pd.DataFrame(car_Horsepower)

fusion = pd.merge(data_frame_price,data_frame_horsepower, on='Company' )

print(fusion)



# ! Tema 3

# * Ejercicio 1

import numpy as np


arrax_4x2 = np.ones((4,2), dtype=np.uint16)

print(arrax_4x2)
print(arrax_4x2.ndim)
print(arrax_4x2.shape)
print(arrax_4x2.itemsize)




# * Ejercicio 2

import numpy as np

matriz = np.arange(100,200,10)

matriz_forma = matriz.reshape(5,2)

print(matriz_forma)


# * Ejercicio 3


import numpy as np

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

tercera_cloum = sampleArray[:,2]

print(tercera_cloum)

# * Ejercicio 4

import numpy as np

sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

columnas_impartes = sampleArray[1::2] #suponiendo que empezamos por 0
columnas_impartes = sampleArray[0::2] #suponiendo que empezamos por 1

print(columnas_impartes)


# * Ejercicio 5

import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])


matriz_tres = (arrayOne + arrayTwo)**2

print(matriz_tres)


# * Ejercicio 6


import numpy as np

matriz = np.arange(10,34,1)

matriz_forma = matriz.reshape(8,3)

matriz_dividida = np.vsplit(matriz_forma,4)


print(matriz_dividida)




# * Ejercicio 7

import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])



ordenado_fila = sampleArray[1,:].argsort()
ordenado_columna = sampleArray[: ,1].argsort()

print(sampleArray[:,ordenado_fila])
print(sampleArray[ordenado_columna,:])


# * Ejercicio 8


import numpy as np


sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

maximo = np.amax(sampleArray, axis=0)
minimo = np.amin(sampleArray, axis=1)

print(maximo)
print(minimo)


# * Ejercicio 9

import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])

sampleArray[:,1] = newColumn

print(sampleArray)


# ! Tema 4

# * Ejercicio 1

import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)


meses = archivo['month_number']
beneficios = archivo['total_profit']


plt.plot(meses, beneficios)
plt.title("Beneficios por mes")
plt.xlabel("Número del mes")
plt.ylabel("Beneficio total")
plt.xticks(meses)
plt.show()


# * Ejercicio 2

import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)


meses = archivo['month_number']
beneficios = archivo['total_profit']


plt.plot(meses, beneficios, linestyle='--', color='red', marker='o', linewidth=3, label="Profit data of last years")
plt.title("Beneficios por mes")
plt.xlabel("Número de mes")
plt.ylabel("Beneficio total")
plt.xticks(meses)
plt.legend(loc='lower right')

plt.show()





# * Ejercicio 3


import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)


facecream = archivo['facecream']
facewash = archivo['facewash']
toothpaste = archivo['toothpaste']
bathingsoap = archivo['bathingsoap']
shampoo = archivo['shampoo']
moisturizer = archivo['moisturizer']
meses = archivo['month_number']

plt.plot(meses,facecream, color='red', marker='o', linewidth=3, label="Sales data facecream")
plt.plot(meses,facewash, color='blue', marker='o', linewidth=3, label="Sales data facewash")
plt.plot(meses,toothpaste, color='green', marker='o', linewidth=3, label="Sales data toothpaste")
plt.plot(meses,bathingsoap, color='black', marker='o', linewidth=3, label="Sales data bathingsoap")
plt.plot(meses,shampoo, color='orange', marker='o', linewidth=3, label="Sales data shampoo")
plt.plot(meses,moisturizer, color='yellow', marker='o', linewidth=3, label="Sales data moisturizer")
plt.title("Venta por productos al mes")
plt.xlabel("Número de meses")
plt.ylabel("Venta total por productos")
plt.legend(loc='upper left')
plt.xticks(meses)
plt.show()



# * Ejercicio 4

import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)

meses = archivo['month_number']
toothpaste = archivo['toothpaste']

plt.scatter(meses, toothpaste, label='Venta de pasta de dientes')
plt.grid(True, linestyle='--')
plt.xticks(meses)
plt.legend(loc='upper left')
plt.title("Venta de pasta de diente")
plt.xlabel("Número de meses")
plt.ylabel("Venta total por pasta de diente")
plt.show()



# * Ejercicio 5


import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)

meses = archivo['month_number']
facewash = archivo['facewash']
facecream = archivo['facecream']

width = 0.5

plt.bar(meses - width/2,facewash, width=width, label="Venta de lavado de cara" )
plt.bar(meses + width/2,facecream, width=width, label="Venta de crema facial" )



plt.grid(True, linestyle='--')
plt.xticks(meses)
plt.legend(loc='upper left')
plt.title("Facewah y facecream ")
plt.xlabel("Número de meses")
plt.ylabel("Venta total producto")
plt.show()


# * Ejercicio 6



import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)

meses = archivo['month_number']
bathingsoap = archivo['bathingsoap']


plt.bar(meses,bathingsoap, label="Jabon de baño" )



plt.grid(True, linestyle='--')
plt.xticks(meses)
plt.legend(loc='upper left')
plt.title("Bathingsoap ")
plt.xlabel("Número de meses")
plt.ylabel("Venta total")
plt.savefig("Grafico_jabon_baño.png")
plt.show()



# * Ejercicio 7

import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)

meses = archivo['month_number']
rango_beneficio = archivo['total_profit'].tolist()

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]

plt.hist(rango_beneficio, bins=profit_range, label="Profit")


plt.legend(loc='upper left')
plt.title("Profit ")
plt.xlabel("Profit en dolares")
plt.ylabel("Actual profit dolares")

plt.show()




# * Ejercicio 8

import pandas as pd
import matplotlib.pyplot as plt


with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r", encoding='utf-8') as file:
    archivo = pd.read_csv(file)



total_productos_vendidos = [float(archivo['facecream'].sum()), float(archivo['facewash'].sum()), float(archivo['toothpaste'].sum()), float(archivo['bathingsoap'].sum()), float(archivo['shampoo'].sum()), float(archivo['moisturizer'].sum())]

nombre_etiquetas = ['Crema facial', 'Limpiador facial', 'Pasta de dientes', 'Jabón de baño', 'Shampoo', 'Crema hidratante']



plt.pie(total_productos_vendidos, labels=nombre_etiquetas, autopct='%1.1f%%')

plt.title('Sales data')

plt.show()

# * Ejercicio 9



import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)

facewash = archivo['facewash']
bathingsoap = archivo['bathingsoap']
meses = archivo['month_number']

plt.subplot(2,1,1)
plt.plot(meses,facewash, color='blue', marker='o', linewidth=3, label="Sales data facewash")
plt.title("Venta por gel de cara al mes")
plt.ylabel("Venta total")
plt.legend(loc='upper left')
plt.xticks(meses)

plt.subplot(2,1,2)
plt.plot(meses,bathingsoap, color='black', marker='o', linewidth=3, label="Sales data bathingsoap")
plt.title("Venta por jabon de baño al mes")
plt.xlabel("Número de meses")
plt.ylabel("Venta total")
plt.legend(loc='upper left')
plt.xticks(meses)
plt.show()





# * Ejercicio 10

import matplotlib.pyplot as plt
import pandas as pd

with open("ejercicios_obligatorio_tema_5/Modulo5_company_sales_data-221102-123259.csv", "r" , encoding="utf-8") as file:
    archivo = pd.read_csv(file)


facecream = archivo['facecream']
facewash = archivo['facewash']
toothpaste = archivo['toothpaste']
bathingsoap = archivo['bathingsoap']
shampoo = archivo['shampoo']
moisturizer = archivo['moisturizer']
meses = archivo['month_number']

plt.stackplot(meses, facecream, facewash,toothpaste,bathingsoap,shampoo,moisturizer, labels=['facecream', 'facewash','toothpaste', 'bathingsoap','shampoo','moisturizer'], colors=['black', 'red', 'blue','orange', 'green','yellow'])

plt.title("Todas las ventas de produdctos en un stack plot")
plt.xlabel("Número de meses")
plt.ylabel("Venta total")
plt.legend(loc='upper left')
plt.xticks(meses)

plt.show()

