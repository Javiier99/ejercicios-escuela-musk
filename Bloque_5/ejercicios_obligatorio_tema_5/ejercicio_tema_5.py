
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




# ! Tema 2

