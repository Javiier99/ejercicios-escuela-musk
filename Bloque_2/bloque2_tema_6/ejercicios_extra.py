


# # ? Crea una función que reciba la información necesaria para calcular el precio final de un producto con IVA incluido y devuelva el precio total.




# def pago_iva_cliente(carrito):
#     iva = 0.21
#     return (carrito * iva) + carrito

# carrito = 32
# pagar_cliente = pago_iva_cliente(carrito)
# print(pagar_cliente)



# # ? Crea una función que, a partir de una lista y un elemento, devuelva cuántas veces aparece ese elemento

# lista = [10,20,30,10,10,50,60,70]
# elemento = 10

# def numero_aparece_elemento():
#     numero_veces_elemento = 0
#     for i in lista:
#         if(i == elemento):
#             numero_veces_elemento += 1
#     return numero_veces_elemento

# resultado = numero_aparece_elemento()

# print(resultado)




# # ? Crea una función que analice un número y devuelva un texto indicando si es par/impar y positivo/negativo/cero. 

# numero = 0

# def analizador_numero(numero):
#     numero_lista = []
#     if((numero % 2) == 0): numero_lista.append("par")
#     elif((numero % 2) != 0): numero_lista.append("impar")
        
#     if(numero > 0): numero_lista.append("positivo")
#     elif(numero < 0): numero_lista.append("negativo")
#     else: numero_lista.append("cero")

#     return numero_lista

# resultado = analizador_numero(numero)

# print(resultado)




# # ? Crea una función que reciba una colección de palabras y un valor numérico, y devuelva solo aquellas palabras cuya longitud sea mayor o igual al valor indicado.

# palabras = ("Palabra" , "Hola", "Mireya", "Elena")

# numeros = 6
# guardar_palabras = []

# def contador_letras(palabras, numeros):
    
#     for i in range(len(palabras)):
#         if(len(palabras[i]) >= numeros):
#             guardar_palabras.append(palabras[i])

# contador_letras(palabras, numeros)

# print(guardar_palabras)



# # ? Diseña varias funciones independientes para trabajar con un diccionario que almacene alumnos y sus notas:
# # ? • Una función que permita añadir una nueva nota a un alumno.
# # ? • Otra que calcule la media de un alumno.
# # ? • Otra que determine qué alumno tiene la mejor media y la devuelva.


# todos_alumnos = {
#     "alumno1": {"nombre" : "javier", "materias" : {"matemáticas" : 10, "lengua" : 7, "historia" : 8, "geografía" : 8}},
#     "alumno2": {"nombre" : "elena", "materias" : {"matemáticas" : 9, "lengua" : 5, "historia" : 4, "geografía" : 5}},
#     "alumno3": {"nombre" : "mireya", "materias" : {"matemáticas" : 9, "lengua" : 6, "historia" : 3, "geografía" : 4}}
# }



# def añadir_nueva_nota(todos_alumnos):
#     nombre_alumno = str(input("A que alumno quieres modificar la nota: ").lower())
#     nombre_materia = str(input(f"A que materia quieres modificar la nota de {nombre_alumno}: ").lower())
#     nota_materia = int(input(f"Que nota le quieres poner a {nombre_materia} del alumno {nombre_alumno} "))
#     for i in range(1, len(todos_alumnos) + 1):
#         if(todos_alumnos[f"alumno{i}"]["nombre"] == nombre_alumno):
#             print(todos_alumnos[f"alumno{i}"]["nombre"])
#             if((nombre_materia == "matematicas") or (nombre_materia == "matemáticas") or (nombre_materia == "mates")):
#                 todos_alumnos[f"alumno{i}"]["materias"]["matemáticas"] = nota_materia
#                 print("Se ha modificado la nota de",todos_alumnos[f"alumno{i}"]["nombre"], f"de la materia Matemáticas a una nota de {nota_materia}")
#                 break
#             elif((nombre_materia == "lengua")):
#                 todos_alumnos[f"alumno{i}"]["materias"]["lengua"] = nota_materia
#                 print("Se ha modificado la nota de",todos_alumnos[f"alumno{i}"]["nombre"], f"de la materia Lengua a una nota de {nota_materia}")
#                 break
#             elif((nombre_materia == "historia")):
#                 todos_alumnos[f"alumno{i}"]["materias"]["historia"] = nota_materia
#                 print("Se ha modificado la nota de",todos_alumnos[f"alumno{i}"]["nombre"], f"de la materia Historia a una nota de {nota_materia}")
#                 break
#             elif((nombre_materia == "geografía") or (nombre_materia == "geografia")):
#                 todos_alumnos[f"alumno{i}"]["materias"]["geografía"] = nota_materia
#                 print("Se ha modificado la nota de",todos_alumnos[f"alumno{i}"]["nombre"], f"de la materia Geografía a una nota de {nota_materia}")
#                 break
#     inicia_sistema(todos_alumnos)


# def calcular_media_alumno(todos_alumnos):
#     nombre_alumno = str(input("A qué alumno quieres calcular la media de sus notas: ")).lower()
#     for i in range(1, len(todos_alumnos) + 1):
#         if(todos_alumnos[f"alumno{i}"]["nombre"] == nombre_alumno):
#             sumario_total = sum(list((todos_alumnos[f"alumno{i}"]["materias"]).values()))
#             media_alumno = sumario_total / len(list(todos_alumnos[f"alumno{i}"]["materias"]))
#             print("La media del alumno", todos_alumnos[f"alumno{i}"]["nombre"], f"es de {media_alumno}")
#     inicia_sistema(todos_alumnos)


# def mejor_alumno(todos_alumnos):
#     nota_media_mas_alta = 0
#     guardar_mejor_alumno = ""
#     for i in range(1, len(todos_alumnos) + 1):
#         nota_alumno = float(sum(list((todos_alumnos[f"alumno{i}"]["materias"]).values())) / (len((todos_alumnos[f"alumno{i}"]["materias"]).values())))
#         if(nota_alumno > nota_media_mas_alta):
#             nota_media_mas_alta = nota_alumno
#             guardar_mejor_alumno = f"El mejor alumno es: {todos_alumnos[f"alumno{i}"]["nombre"]}, con una nota media de {sum(list((todos_alumnos[f"alumno{i}"]["materias"]).values()))/ (len((todos_alumnos[f"alumno{i}"]["materias"]).values()))}"
#     print(guardar_mejor_alumno)



# def inicia_sistema(todos_alumnos):
#     while True:
#         iniciar_sistema_pregunta = str(input("¿Dime que quieres hacer: Añadir nueva nota: 1, Calcular Media Alumno: 2, Saber el mejor alumno: 3, Cerrar la sesión: 4? ")).lower()
#         if((iniciar_sistema_pregunta == "1") or ("añadir nueva nota" == iniciar_sistema_pregunta)):
#             añadir_nueva_nota(todos_alumnos)
#         elif((iniciar_sistema_pregunta == "2") or ("calcular media alummno" == iniciar_sistema_pregunta)):
#             calcular_media_alumno(todos_alumnos)
#         elif((iniciar_sistema_pregunta == "3") or ("mejor alumno" == iniciar_sistema_pregunta)):
#             mejor_alumno(todos_alumnos)
#         elif((iniciar_sistema_pregunta == "4")):
#             break
#         else:
#             print("No te entiendo")


# inicia_sistema(todos_alumnos)




# # ? Crea varias funciones para analizar un texto:
# # ? • Una que devuelva cuántas palabras contiene.
# # ? • Otra que devuelva cuántas letras tiene (sin contar espacios).
# # ? • Otra que devuelva la palabra más larga


# texto_analizar = str(input("Escribe un texto ")) 


# # * Contador de palabras

# def numero_palabras_contiene(texto_analizar):
#     texto_analizar_lista = texto_analizar.split(" ")
#     contador_palabras_lista = len(texto_analizar_lista)
#     print(f"En el texto contiene exactamente {contador_palabras_lista} palabras")

# # * Contador de letras

# def numero_letras_contiene(texto_analizar):
#     texto_sin_espacios = texto_analizar.replace(" ","")
#     contador_letras = len(texto_sin_espacios)
#     print(f"El texto contiene exactamente {contador_letras} letras sin contar los espacios")


# # *Devolver la palabra más larga
# def palabra_mas_larga(texto_analizar):
#     numero_palabra_larga = 0
#     guardar_palabra_larga = ""
#     texto_analizar_lista = texto_analizar.split(" ")
#     for i in range(len(texto_analizar_lista)):
#         if(numero_palabra_larga < len(texto_analizar_lista[i])):
#             guardar_palabra_larga = texto_analizar_lista[i]
#     print(f"La palabra más larga del texto es: {guardar_palabra_larga}")


# numero_palabras_contiene(texto_analizar)
# numero_letras_contiene(texto_analizar)
# palabra_mas_larga(texto_analizar)


















