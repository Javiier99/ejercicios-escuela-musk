

# ! Se puede crear nuevos archivos de esta forma además con nombres personalizados

# nombre_cliente = str(input("Dime un nombre para el archivo "))

# try:
#     # ! Si queremos tener una carpeta única para abrirlo debemos de colocar la carpeta junto con el nombre del archivo que querramos crear/abrir, etc
#     file = open(f"Bloque_5/{nombre_cliente}", "w")
#     file.write("Hola este es un archivo de texto")


# finally:
#     file.close()








# with open("bloque_5/javier" , "a+") as file:
#     # file.write("Hola como estas \n")
#     file.seek(0)
#     for i in range(4):
#         primera_linea = file.readline()
#         print(f"Primera linea: {primera_linea.strip()}")





with open("bloque_5/achivo.txt" , "r") as file: # * Abrimos el archivo y lo definimos como "file" se puede definir como quieras
    hola = file.readline().strip() # * Una vez definido usamos ese nombre que le damos junto con el método que querramos.
    hola2 = file.readline().strip() # * Una vez definido usamos ese nombre que le damos junto con el método que querramos.
    print(hola)
    print(hola2)
    print(file.readline().strip())

















