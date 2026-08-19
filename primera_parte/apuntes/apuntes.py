
# palabra = "Hola como estás"

# print(palabra[1])
# print(palabra[2:7])
# print(palabra[:5])
# print(palabra in "como")
# print("como" in palabra)




# palabra = "Hola como estás"
# palabras = ["Hola","como","estás"]



# print(palabra.capitalize())
# print(palabra.title())
# print(palabra.upper())
# print(palabra.lower())
# print(palabra.replace("como","Viva España"))
# print(palabra.split())
# print("-".join(palabras))




# palabra = "Hola como estás"

# print(palabra.index("estás"))


# lista = ["apple", "banana", "cherry"]
# lista.insert(-1,"orange")
# lista.insert(-1,"hola")
# print(lista)


# TUPLA_CORRECTA = ("Apple", )
# TUPLA_INCORRECTA = ("Apple")

# print(type(TUPLA_CORRECTA))
# print(type(TUPLA_INCORRECTA))





# objeto = {
#     "nombre" : "Javier",
#     "apellido" : "Delgado Rodríguez",
#     "edad" : 27
# }


# print(f"Hola {objeto.get("nombre")}")




# mi_dicionario = {"nombre":"Isabel","edad":30,"pais":"España"}
# nombre = mi_dicionario["nombre"]
# mi_dicionario["edad"] = "edad"
# print(f"Mi nombre es {nombre}")








# #  1  Referentes a voltear palabras:

# cadena = str(input("Palabra "))

# cadena_volteada = "".join(reversed(cadena))

# print(cadena_volteada)


# numero = "123"
# numero_volteado = "".join(reversed(numero))
# print(numero_volteado)

# set7 = {10, 20, 30, 40, 50}
# set8 = {30, 40, 50, 60, 70}

# set6 = set7.symmetric_difference(set8)

# print(set6)



# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.intersection_update(set2)

# print(set1)




# nombre = str(input("Dime tu nombre"))

# def saludar(nombre):
#     print(f"Hola {nombre}")


# saludar(nombre)




# import sys
# sys.path.append(r'c:\MUSK/apuntes') 

# from ejemplo import viva_españa

# # from ejemplo import viva_españa 


# print(viva_españa())




# def resta: ()




# * Programación orientada a objetos


# class Coche:
#     def desplazarse(self):
#         print("El coche avanza usando cuatro ruedas y un motor de combustión.")

# class Bicicleta:
#     def desplazarse(self):
#         print("La bicicleta avanza mediante el pedaleo del usuario.")

# class Gato:
#     def desplazarse(self):
#         print("El gato se desplaza caminando silenciosamente sobre sus cuatro patas.")

# # Una función que no necesita saber el tipo exacto, solo invoca la acción común
# # Esto es la aplicación pura del Polimorfismo
# def iniciar_movimiento(entidad):
#     entidad.desplazarse()

# # Colección con objetos de naturaleza completamente dispar
# elementos = [Coche(), Bicicleta(), Gato()]

# for x in elementos:
#     iniciar_movimiento(x)

# # Salidas consecutivas en consola:
# # -> El coche avanza usando cuatro ruedas y un motor de combustión.
# # -> La bicicleta avanza mediante el pedaleo del usuario.
# # -> El gato se desplaza caminando silenciosamente sobre sus cuatro patas.







# class Cookie:
#     pass

# c1 = Cookie()
# c2 = Cookie()

# print(c1)
# print(c2)






# * Apuntes relacionado Bloque 3



# class Coche:
#     def __init__(self, color, marca, numero_puertas, numero_ruedas):
#         self.color = color
#         self.marca = marca
#         self.numero_puertas = 3
#         self.numero_ruedas = 4




# coche1 = Coche("rojo", "mercedes","","")
# coche2 = Coche("azul", "Kia","",3)

# coche1.numero_ruedas = 2

# print(coche1.numero_ruedas)
# print(coche2.numero_ruedas)


# # * Atributos de clase


# class Persona:
#     raza = "Humano"
#     def __init__(self, nombre):
#         self.nombre = nombre
#         pass
# humano1 = Persona("Javier")

# print(Persona.raza) #De esta forma llamamos a un atributo de clase
# print(humano1.nombre) #De esta forma llamamos a una instancia







# * Métodos de instancias



# class Coche:
#     def __init__(self, nombre, num_ruedas, edad):
#         self.nombre = nombre
#         self.num_ruedas =  num_ruedas
#         self.edad = edad
    
#     # * Método de instancia:
#     def conducir(self, direccion):
#         return direccion
#     def marcha_atras(self,direccion):
#         self.num_ruedas = self.num_ruedas + 5
#         self.direccion = direccion
#         return f"Nos vamos a {self.direccion} con {self.num_ruedas} ruedas"
#     def año_coche(self):
#         self.edad = self.edad + 1
#     def pasar_itv(self):
#         toca_pasar_itv = False
#         if(self.edad >= 5):
#             toca_pasar_itv = True

#         else:
#             toca_pasar_itv = False

#         return toca_pasar_itv

# coche1 = Coche("Mercedes", 3, 4)

# # print(coche1.conducir("Dirección Huelva"))
# # print(coche1.conducir("Dirección Sevilla"))
# # print(coche1.marcha_atras("Granada"))

# # print(coche1.edad)
# coche1.año_coche()
# # print(coche1.edad)

# print(f"Ya puedes hacer {coche1.pasar_itv()}")
















hola = 3
print(hola + 3)

































































































