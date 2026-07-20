
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



# * Ejercicio 5

def display_words(file):
    texto_dividido = file.read().split()
    mostrar_palabras = []
    for i in range(len(texto_dividido)):
        contador_letras= len(texto_dividido[i])

        if(contador_letras < 4):
            mostrar_palabras.append(texto_dividido[i])

    return mostrar_palabras

with open("ejercicios_obligatorio_tema_5/archivos_creados/historia.txt", "r", encoding="utf-8") as file:
    
    resultado = display_words(file)
    
    print(f"Palabras con menos de 4 caracteres: {resultado}")


# * Ejercicio 6
