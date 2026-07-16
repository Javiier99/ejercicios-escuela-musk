

# class Estudiantes():

#     def __init__(self, nombre):
#         self.nombre = nombre




# class Clases(Estudiantes):
#     def __init__(self, nombre, clases):
#         super().__init__(nombre)
#         self.clases = clases

#     def decir_hola(self):
#         print(f"El alumno {self.nombre} dice Hola a la clase {self.clases}")


# alumno1 = Estudiantes("Javier")
# alumno2 = Clases(alumno1.nombre, 7)



# # alumno2.decir_hola()


# # print(Clases.mro())

# print(issubclass(Clases, Estudiantes ))





# # ! Clases abstractas

# from abc  import ABC, abstractmethod

# class Animal(ABC): # * Heredará de ABC

#     def caminar_4_patas(self): # * No necesito escribir dos veces en Perro y Gato porque ambos objetos hacen lo mismo, que es caminar a 4 patas
#         print("Camina a 4 patas")

#     @abstractmethod #* Queremos que sea abstracta porque cada animal hace un tipo de sonido diferente
#     def hacer_sonido(self):
#         pass
    


# class Perro(Animal):

#     def hacer_sonido(self):
#         print("Guau")


# class Gato(Animal):
    

#     def hacer_sonido(self):
#         print("Miau")

# perro = Perro()
# perro.caminar_4_patas()
# perro.hacer_sonido()

# gato = Gato()
# gato.caminar_4_patas()
# gato.hacer_sonido()









# # ! Decoradores

# def inicio_sesion(func):
#     def wrapper(): # * Lo podemos llamar como querramos, pero se llama wrapper(envoltorio) entre programadores para entendernos
#         # 1. El decorador prepara los datos que se van a comprobar
#         usuario_introducido = "javier"
#         contrasena_introducida = 123
        
#         print("Decorador: Enviando datos a comprobar...")
        
#         # 2. Ejecutamos la función pasándole los datos y GUARDAMOS lo que devuelve
#         ha_entrado = func(usuario_introducido, contrasena_introducida)
        
#         # 3. El decorador actúa según el resultado de la función
#         if ha_entrado: # Es lo mismo que: if ha_entrado == True
#             print("Decorador: ¡Acceso concedido! Bienvenido al sistema.")
#         else:
#             print("Decorador: ¡Acceso denegado! Datos incorrectos.")
            
#         return ha_entrado # Devolvemos el resultado hacia afuera
        
#     return wrapper


# @inicio_sesion
# def usuario_contraseña(usuario, contraseña):
#     # Esta función SOLO se encarga de decir si los datos coinciden o no
#     if usuario == "javier" and contraseña == 123:
#         return True
#     else:
#         return False

# # --- Ejecución ---
# # Llamamos a la función vacía porque el decorador ya le inyecta los datos dentro
# usuario_contraseña()





# @inicio_sesion
# def otra_cosa(usuario, contraseña):
#     # Esta función SOLO se encarga de decir si los datos coinciden o no
#     if usuario == "javier" and contraseña == 123:
#         return True
#     else:
#         return False

# # --- Ejecución ---
# # Llamamos a la función vacía porque el decorador ya le inyecta los datos dentro
# otra_cosa()








# ! Datos  temporales

# from datetime import date

# d = date.today()
# print(d)


# from datetime import time

# print(time(hour=23, minute=22,second=2))
# print(time(0,4,5))



from datetime import datetime,date, timedelta
from zoneinfo import ZoneInfo

# zona = ZoneInfo("Europe/Madrid")
# fecha = datetime.now(zona)

# print(fecha)


# d1 = date(2023,3,10)
# print(d1)

# print(date.min)
# print(date.max)




# fecha_hora = datetime.now().time().minute


# parar = False
# contador =  0
# while parar == False:
    
#     fecha_hora = datetime.now().time().minute
#     print(contador)
    
#     contador += 3
#     contador -= 2
#     if(fecha_hora == 57):
#         parar = True

# print(fecha_hora)






# mañana = date.today() + timedelta(days=1)

# import datetime

# tiempo_restante = datetime.datetime()
# print(tiempo_restante)




# def contador(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1

# for num in contador(5):
#     print(num)





# def mi_generador():
#     print("-> Empezamos la función")
#     yield "Primer Juguete"
    
#     print("-> Continuamos después de la primera pausa")
#     yield "Segundo Juguete"
    
#     print("-> Último tramo")
#     yield "Tercer Juguete"

# # Al llamarla, NO se ejecuta el código. Se crea el objeto generador.
# fabrica = mi_generador()

# # Para pedirle valores, usamos la función next() o un bucle for
# print(next(fabrica)) 
# # Salida:
# # -> Empezamos la función
# # Primer Juguete

# print(next(fabrica))
# # Salida:
# # -> Continuamos después de la primera pausa
# # Segundo Juguete

# print(next(fabrica))













# lista = [1,2,3,4,5,6,7,8,9,0]

# def sin_generador(lista):
#     guardar = ""
#     for i in lista:
#         i = str(i)
#         guardar += i
#     return guardar

# # print(sin_generador(lista))



# lista = [1,2,3,4,5,6,7,8,9,0] #*  Aquí recibimos cualquier dato, la cuestión de usar los generadores es cuando tengamos una cantidad inimaginable de datos

# def con_generador(lista): # * Empezamos a crear el generador, siempre con una función
#     for i in lista:
#         i = str(i)
#         yield i # * Cuando tengamos el dato que nosotros querremos, lo colocamos con yield 

# mi_generador = con_generador(lista) # * Teniendo yield debemos de guardar todo en una variable, y esta variale debe de estar fuera de la función
# mi_generador_2 = con_generador(lista)


# for numero_str in mi_generador: # * Esta es la manera más optima de mostrar los datos con yield
#     print(numero_str)
#     pass


# primer_dato = next(mi_generador_2) # * con next podemos obtener un dato en concreto y así lo podremos dividir en variables
# segundo_dato = next(mi_generador_2)
# print(primer_dato)
# print(segundo_dato)









# def mi_sensor():
#     print("-> El sensor se ha encendido y está esperando órdenes...")
#     while True:
#         # Aquí el yield hace una pausa. 
#         # Cuando uses .send("hola"), la palabra "hola" se guardará en la variable 'orden'
#         orden = yield "Aquí tienes un dato de temperatura"
        
#         print(f"-> ¡He recibido la orden externa!: {orden}")

# # 1. Creamos el generador
# sensor = mi_sensor()

# # 2. OBLIGATORIO: La primera vez hay que usar next() para arrancar el motor
# next(sensor) 

# print("--- Ahora vamos a usar .send() desde fuera ---")

# # 3. AQUÍ ES DONDE SE PONE EL .SEND()
# # Le mandamos la palabra "pausa" al generador
# sensor.send("pausa")

# # Le mandamos la palabra "reanudar" al generador
# sensor.send("reanudar")












def maquina_de_escupir():
    yield "Caramelo de fresa"
    yield "Caramelo de menta"

objeto = maquina_de_escupir()

# Con next() solo SACAS información
# print(next(objeto))  # Imprime: Caramelo de fresa







# def maquina_interactiva():
#     print("1. Arranco la máquina...")
    
#     # La máquina escupe "Hola" y SE CONGELA esperando un dato.
#     # El dato que tú le envíes desde fuera se guardará en 'lo_que_tu_me_mandes'
#     lo_que_tu_me_mandes = yield "Hola"
    
#     # La máquina se despierta y usa el dato que tú le metiste
#     print(f"3. He despertado. Me has mandado esto desde fuera: {lo_que_tu_me_mandes}")
#     yield "Adiós"

# # --- CÓMO SE USA DESDE FUERA ---

# objeto = maquina_interactiva()

# # PASO A: Obligatorio arrancar con next() para que llegue al primer yield
# print(next(objeto))  # Imprime: Hola (la máquina se duerme aquí)

# # PASO B: ¡AQUÍ USA SUBIDAMENTE EL .SEND()!
# # Le metemos el texto "Perrito caliente" dentro de la máquina en marcha
# print(objeto.send("Perrito caliente"))

# import random


# def prueba():
#     while True: 
#         un_dato = random.random()
#         print("Arrancamos la maquina")

#         lo_que_quieras = yield un_dato
#         print("Ha despertado", lo_que_quieras)
#         # yield "Adios"

# objeto = prueba()

# valor = next(objeto)

# print("El valor es",valor)

# def bucle():
#     contador = 0
#     parar = True
#     while parar == True:
#         nuevo_argumento = "El numero nuevo es: ", contador
#         nuevo_valor = objeto.send(nuevo_argumento)
#         print("El nuevo valor es: ", nuevo_valor)
#         contador += 1
#         if(contador == 20):
#             parar = False



# bucle()


































# mi_lista = ["Manzanas", "Leche", "Papel higiénico", "Pollo", "Café", "Queso"]

# def maquina_compra():
#     while True:
#         if(len(mi_lista) == 0):
#             break
#         elif(len(mi_lista) != 0):
#             dato_cogido = mi_lista.pop(0)

#             print(f"El usuario ha cogido {dato_cogido}")

#             dato_enviado = yield dato_cogido

#             print(f"Primer producto: {dato_enviado} tachado de la lista")


# objeto_elegido_para_cogerlo_de_la_tienda = maquina_compra()
# productos = next(objeto_elegido_para_cogerlo_de_la_tienda)


# def meter_carrito():
#     # contador = 0
#     parar = True
#     while parar == True:
#         # contador += 1
#         if(len(mi_lista) == 0):
#             break
#         elif(len(mi_lista) != 0):

#             objeto_de_la_compra_cogido = objeto_elegido_para_cogerlo_de_la_tienda.send("Se ha guardado en el carrito el objeto")
#             print("Se ha cogido el objeto", objeto_de_la_compra_cogido)
#         # if(contador == 4):
#         #     parar = False


# meter_carrito()















# Ejercicio correcto


# # ! Código escrito por mi en un 90% el resto IA

# # ! ejercicio vamos a encadenar una cadena de supermercados, empezaremos desde la fabricación de los productos, pasaremos por la distribución, que llegará al super y finalmente al cliente


# # *Lista de productos:
# productos = [
#     "Leche",
#     "Pan",
#     "Huevos",
#     "Arroz",
#     "Pasta",
#     "Aceite de oliva",
#     "Azúcar",
#     "Sal",
#     "Harina",
#     "Tomates",
#     "Cebollas",
#     "Patatas",
#     "Manzanas",
#     "Plátanos",
#     "Pollo",
#     "Carne picada",
#     "Atún en lata",
#     "Queso",
#     "Yogur",
#     "Mantequilla",
#     "Café",
#     "Té",
#     "Cereales",
#     "Galletas",
#     "Agua mineral",
#     "Refresco de cola",
#     "Detergente",
#     "Papel higiénico",
#     "Jabón de manos",
#     "Pasta de dientes"
# ]

# # * Aquí debemos de colocar la fabrica donde se fabricarán los productos, en caso de no haber más se para

# def fabrica():
#     contador = 0
#     while len(productos) > 0:
#         contador += 1
#         un_producto = productos.pop(0)
#         print(f"Tenemos el {contador} de la fabrica de producto que es: {un_producto}")
#         yield un_producto
#         print("Pasamos al siguiente producto")
#     print("No quedan más materias primas")


# # * Aquí la fabrica de los productos lo llevará a la empresa distribuidora, y se guardará dichos datos, hasta que sean usados, en caso de no haber más se para
# # * El distribuidor no enviará paquetes hasta que tenga una cantidad que le salga rentable, que son 5 productos



# def distribuidor(generador_fabrica):
#     distribuidor_objetos_guardados = []
#     for producto in generador_fabrica:
#         distribuidor_objetos_guardados.append(producto)

#         if(len(distribuidor_objetos_guardados) >= 5 ):
#             print(f"[DISTRIBUIDOR] Lote de {len(distribuidor_objetos_guardados)} listo. Enviando carga...")
            
#             yield distribuidor_objetos_guardados
#             distribuidor_objetos_guardados = []
#             print("Siguiente producto a enviar por el distribuidor")

#         else:
#             print("El distribuidor todavía no posee los productos justos, nos ponemos a la espera")



# # * Aquí todos los productos de la empresa distribuidora se enviarán a los supermercado y se guarda ahí

# productos_supermercados = []

# def supermercado(generador_distribuidor):
#     for lote in generador_distribuidor:
#         print(f"[SUPERMERCADO] ¡Ha llegado un lote de productos! {lote}")
#         for prod in lote:
#             productos_supermercados.append(prod)
#             yield productos_supermercados
#             print(f"Los productos están en la estantería {productos_supermercados}")



# # * Aquí la persona normal coge los productos

# lista_cliente = [
#     "Sal",
#     "Harina",
#     "Tomates",
#     "Cebollas",
#     "Patatas",
#     "Manzanas",
#     "Plátanos",
#     ]
# objeto_guardado_carrito = []


# instancia_fabrica = fabrica()
# instancia_distribuidor = distribuidor(instancia_fabrica)
# instancia_supermercado = supermercado(instancia_distribuidor)

# def cliente():
#     for estanteria in instancia_supermercado:

#         for producto_deseado in list(lista_cliente):
#             if producto_deseado in estanteria:
#                 lista_cliente.remove(producto_deseado)
#                 estanteria.remove(producto_deseado)
#                 objeto_guardado_carrito.append(producto_deseado)
#                 print(f"El cliente encontro su {producto_deseado}")

# clientes = cliente()

# if(len(lista_cliente) == 0):
#     print(f"Exito el cliente ha comprado toda su lista {objeto_guardado_carrito}")




























# ! El codigo escrito por mi, sin IA, está medio bien, el bueno está arriba






# # *Lista de productos:
# productos = [
#     "Leche",
#     "Pan",
#     "Huevos",
#     "Arroz",
#     "Pasta",
#     "Aceite de oliva",
#     "Azúcar",
#     "Sal",
#     "Harina",
#     "Tomates",
#     "Cebollas",
#     "Patatas",
#     "Manzanas",
#     "Plátanos",
#     "Pollo",
#     "Carne picada",
#     "Atún en lata",
#     "Queso",
#     "Yogur",
#     "Mantequilla",
#     "Café",
#     "Té",
#     "Cereales",
#     "Galletas",
#     "Agua mineral",
#     "Refresco de cola",
#     "Detergente",
#     "Papel higiénico",
#     "Jabón de manos",
#     "Pasta de dientes"
# ]

# # * Aquí debemos de colocar la fabrica donde se fabricarán los productos, en caso de no haber más se para

# def fabrica():
#     contador = 0
#     while True:
#         contador += 1
#         if(len(productos) != 0):
#             un_producto = productos.pop(0)
#         else: 
#             break
#         print(f"Tenemos el {contador} de la fabrica de producto que es: {un_producto}")
#         producto_fabrica = yield un_producto
#         print("Pasamos al siguiente producto")

# la_fabrica = fabrica()
# objeto_fabrica = next(la_fabrica)

# # * Aquí la fabrica de los productos lo llevará a la empresa distribuidora, y se guardará dichos datos, hasta que sean usados, en caso de no haber más se para
# # * El distribuidor no enviará paquetes hasta que tenga una cantidad que le salga rentable, que son 5 productos

# distribuidor_objetos_guardados = []

# def distribuidor():
#     while True:
#         objeto_distribuidor = la_fabrica.send(f"Se ha obtenido este producto {la_fabrica}")
#         distribuidor_objetos_guardados.append(objeto_distribuidor)
#         if(len(distribuidor_objetos_guardados) >= 5 ):
#             print("El distribuidor posee los productos justos para que le salga rentable enviar una carga al supermercado")
#             producto_individual_enviado = distribuidor_objetos_guardados.pop(0)
#             producto_distribuidor = yield producto_individual_enviado
#             print("Siguiente producto a enviar por el distribuidor")

#         else:
#             print("El distribuidor todavía no posee los productos justos, nos ponemos a la espera")

# el_distribuidor = distribuidor()
# objetos_enviados_distribuidor = next(el_distribuidor)

# # * Aquí todos los productos de la empresa distribuidora se enviarán a los supermercado y se guarda ahí

# productos_supermercados = []

# def supermercado():
#     while True:
        
#         print("Los productos enviados han llegado al super")
#         objetos_distribuidor_super = next(el_distribuidor,None)
        
#         if(objetos_distribuidor_super is None):
#             print("No quedan más productos de fabrica")
#             break
        
#         productos_supermercados.append(objetos_distribuidor_super)
#         productos_super = yield productos_supermercados
#         print(f"Los productos están en la estantería {productos_supermercados}")

# el_super = supermercado()
# objetos_super = next(el_super)

# # * Aquí la persona normal coge los productos

# lista_cliente = [
#     "Sal",
#     "Harina",
#     "Tomates",
#     "Cebollas",
#     "Patatas",
#     "Manzanas",
#     "Plátanos",
#     ]
# objeto_guardado_carrito = []

# def cliente():
#     while True:
#         if(len(lista_cliente) != 0):
#             for i in range(len(lista_cliente)):
#                 for x in range(len(productos_supermercados)):
#                     if(lista_cliente[i] == productos_supermercados[x]):
#                         lista_cliente.remove(lista_cliente[i])
#                         productos_supermercados.remove(productos_supermercados[x])
#                         objeto_guardado_carrito.append(productos_supermercados[x])
#                         objeto_a_enviar = yield objeto_guardado_carrito
#                     else:
#                         next(la_fabrica)
#                         next(el_distribuidor)
#                         next(el_super)
                        

#         else:
#             print(f"La lista está completa, aquí tenemos el carrito {objeto_guardado_carrito}")
#             break

# clientes = cliente()
# while len(lista_cliente) != 0:
    
#     los_clientes = next(clientes)
#     if(len(lista_cliente) == 0):
#         print(f"La lista está completa, aquí tenemos el carrito {objeto_guardado_carrito}")
#         break

























# lista = [1,2,3,4,5,6,7,8]

# for i in range(20):


    
#     try:
#         lista[i]
#         print("Funciona")
#     except:
#         print("Ya no funciona")



numero = 4
try:

    resultado = 10/(numero - 4) 
    print(resultado)
except ZeroDivisionError:
    print("Hola")








