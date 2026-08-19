
# # ! Ejercicio 1

# poema = ["Primera estrofa del poema", "Segunda estrofa", "Tercera estrofa", "El final del texto"]


# with open("bloque_5/ejercicio_opcional/poema.txt", "a") as file:
#     for i in poema:
#         file.write(f"{i} \n")


# with open("bloque_5/ejercicio_opcional/poema.txt", "r") as file:
#     file.read()


# nueva_lista = []


# with open("bloque_5/ejercicio_opcional/poema.txt", "r") as file:
#     try:
#         parar = True
#         while parar == True:
#             fila_documento = file.readline()
#             if(fila_documento == ""):
#                 parar = False
#             else:
#                 nueva_lista.append(fila_documento)

#     except:
#         print("Hemos terminado de guardar todo")



# for i in nueva_lista:
#     print(i, end="")




# # ! Ejercice 2



# with open("Bloque_5/ejercicio_opcional/ejercice_2.txt" , "w") as file:
#     file.write("Start registration")


# with open("Bloque_5/ejercicio_opcional/ejercice_2.txt", "w") as file:
#     file.write("Update your resgistration now \n")


# with open("Bloque_5/ejercicio_opcional/ejercice_2.txt", "a") as file:
#     file.write("add an event later \n")



# # ! Ejercice 3




# with open("Bloque_5/ejercicio_opcional/numeros.txt" , "w") as file:
#     for i in range(30):
#         file.write(f"{i}\n")



# with open("Bloque_5/ejercicio_opcional/numeros.txt" , "r") as file:
#     linea = None
#     while linea != "":
#         linea = file.readline().strip()
#         print(linea)




















