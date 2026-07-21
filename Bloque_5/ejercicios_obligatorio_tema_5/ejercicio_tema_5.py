
# ! Tema 1

# # * Ejercicio 1

# with open("ejercicios_obligatorio_tema_5/archivos_creados/poema.txt", "r", encoding="utf-8") as file:
#     for i in file:
#         print(i.strip())
    


# # * Ejercicio 2

# with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:
#     lineas = file.readlines()
#     numero_lineas = len(lineas)
#     print(numero_lineas)



# # * Ejercicio 3


# with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:

#     frases = file.readlines()

#     contador = 0
#     for i in frases:
#         numero_palabras = len(i.split())
#         contador += numero_palabras
#     print(contador)


# # * Ejercicio 4

# with open("ejercicios_obligatorio_tema_5/archivos_creados/notas.txt", "r", encoding="utf-8") as file:
#     contador_el = []
#     num_contador_el = 0
#     frase_entera = file.read()
#     frase_dividida = frase_entera.split()
#     contador = 0
#     for i in range(len(frase_dividida)):
#         palabras = frase_dividida[i]
#         contador += 1
#         if(palabras == "el") or (palabras == "El"):
#             contador_el.append(contador)
#             num_contador_el += 1
    
#     print(f'Tenemos {num_contador_el} "el" y sus posiciones son {contador_el}')



# # * Ejercicio 5

# def display_words(texto_dividido):
#     mostrar_palabras = []
#     for i in range(len(texto_dividido)):
#         contador_letras= len(texto_dividido[i])

#         if(contador_letras < 4):
#             mostrar_palabras.append(texto_dividido[i])

#     return mostrar_palabras

# with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:
#     texto_dividido = file.read().split()
#     resultado = display_words(texto_dividido)
    
#     print(f"Palabras con menos de 4 caracteres: {resultado}")


# # * Ejercicio 6


# def hash_display(todo_texto, letra_especial):
#     resultado_lista = []
#     list_texto = todo_texto.split()
#     for i in list_texto:
#         guardar_texto = ""
#         for x in range(len(i)):
#             guardar_texto += i[x].join(f" {letra_especial}")
#         sin_espacios = guardar_texto.replace(" ", "")
#         resultado_lista.append(sin_espacios)
#     texto = " ".join(resultado_lista)
#     return texto


# letra_especial = str(input("¿Qué letra especial quieres poner? "))

# with open("ejercicios_obligatorio_tema_5/archivos_creados/materia.txt", "r", encoding="utf-8") as file:
#     todo_texto = file.read().strip()
#     resultado = hash_display(todo_texto, letra_especial)
    
#     print(resultado)


# # * Ejercicio 7


# import string

# for i in range(len(string.ascii_uppercase)):
#     with open(f"ejercicios_obligatorio_tema_5/archivos_creados/generador_archivo_ejercicio_7/{string.ascii_uppercase[i]}.txt", "w", encoding="utf=8") as file:
#         file.write(f"{string.ascii_uppercase[i]}")



# # * Ejercicio 8

# with open("ejercicios_obligatorio_tema_5/archivos_creados/python.txt", "a" , encoding="utf-8") as file:
#     file.write("Cualquier texto")

# with open("ejercicios_obligatorio_tema_5/archivos_creados/python.txt", "r" , encoding="utf-8") as file:
#     print(file.read())



# # * Ejercicio 9

# with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt" , "r", encoding="utf-8") as file:
#     texto_completo = file.read().split()
# contador_palabras = []
# for i in range(len(texto_completo)):
#         palabra_contabilizada = False
#         for x in range(len(contador_palabras)):
#             if(contador_palabras[x][0].lower() == texto_completo[i].lower()):
#                 contador_palabras[x][1] += 1
#                 palabra_contabilizada = True
        
#         if(palabra_contabilizada == False):
#                 contador_palabras.append([texto_completo[i].lower() ,1])


# print(contador_palabras)


# # * Ejercicio 10

# from pathlib import Path


# archivo_encontrados = list(Path(".").rglob("notas.txt"))

# if(archivo_encontrados):
#     for i in archivo_encontrados:
#         print(f"El archivo existe, está {i}")

# else:
#     print("El archivo no existe")




# # ! Tema 2

# # * Ejercicio 1

# import csv

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding="utf-8") as file:
#     lineas = csv.reader(file)
#     cabecera = next(lineas)
#     contador_5_primeras_lineas = 0
#     contador_5_ultimas_lineas = 0
#     for i in lineas:
#         print(i)
#         contador_5_primeras_lineas += 1
#         if(contador_5_primeras_lineas == 5):
#             break
#     lineas_listas = list(lineas)
#     for i in reversed(lineas_listas):
#         print(i)
#         contador_5_ultimas_lineas += 1
#         if(contador_5_ultimas_lineas == 5):
#             break


# # * Ejercicio 2

# import csv

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding="utf-8") as file:
#     archivo =  list(csv.DictReader(file))

# # cabecera = next(archivo)

# # 1 Dado que no hay ningún dato que sea Nan, crearé una columna nueva y lo pondré alli para posteriormente cambiarlo por otro dato 

# for i in archivo:
#     i['nueva_columna'] = None

# cabecera = ['','index','company','body-style','wheel-base','length','engine-type','num-of-cylinders','horsepower','average-mileage','price','nueva_columna']

# # 1 Escribimos una nueva columna
# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "w", newline='', encoding="utf-8") as file:
#     escribir = csv.DictWriter(file, fieldnames=cabecera)
#     escribir.writeheader()
#     escribir.writerows(archivo)

# # 1 Sustituimos la nueva el texto nan, por otro con un condicional

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", newline='', encoding="utf-8") as file:
#     archivo_cambiado = list(csv.DictReader(file))

# for i in archivo_cambiado:
#     if(i['company'] == 'honda'):
#         i['nueva_columna'] = "Esto es una sustitución"

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "w", newline='', encoding="utf-8") as file:
#     escribir = csv.DictWriter(file, fieldnames=cabecera)
#     escribir.writeheader()
#     escribir.writerows(archivo_cambiado)



# # * Ejercicio 3

# import csv

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv", "r", encoding='utf-8') as file:
#     archivo_leido = list(csv.DictReader(file))

# guardar_dato = {'Nombre Empresa' : '', 'Precio' : 0, 'Posición' : 0}
# contador = 1 # Tenemos 1 ya que empezamos contando la cabecera
# for i in archivo_leido:
#     try:
#         precio_csv = float(i['price'])
#         if(precio_csv > guardar_dato['Precio']):
#             guardar_dato['Nombre Empresa'] = i['company']
#             guardar_dato['Precio'] = precio_csv
#             guardar_dato['Precio'] = precio_csv
#             guardar_dato['Posición'] = contador + 1 # le sumamos 1 ya que el contador está al final y no llega a contar
            
        
#         contador += 1
#     except ValueError:
#         contador += 1
#         continue
    

# print(f"La empresa con el coche más caro es {guardar_dato['Nombre Empresa']} y su precio es: {guardar_dato['Precio']}€ su posición es: {guardar_dato['Posición']}")



# # * Ejercicio 4

# import csv
# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
#     archivo = list(csv.DictReader(file))


# for i in archivo:
#     if(i['company'] == 'toyota'):
#         print(i)


# # * Ejercicio 5

# import csv
# from collections import Counter

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
#     archivo = list(csv.DictReader(file))

# empresas = []
# for i in archivo:
#     empresas.append(i['company'])

# conteo_empresas = Counter(empresas)

# # * Ejercicio 6

# import csv
# from collections import Counter

# with open("ejercicios_obligatorio_tema_5/Modulo5_Automobile_data-221102-123259.csv" , "r" , encoding='utf-8') as file:
#     archivo = list(csv.DictReader(file))


# guardar_marca_precio_altos = {}

# for coches in archivo:
#     empresa = coches['company']
#     try:
#         precio = float(coches['price'])
#     except:
#         precio = 0.0

    
#     if ((empresa not in guardar_marca_precio_altos) or (precio > guardar_marca_precio_altos[empresa])):
#         guardar_marca_precio_altos[empresa] = precio

# print(guardar_marca_precio_altos)




# * Ejercicio 7


















































































































































































































































