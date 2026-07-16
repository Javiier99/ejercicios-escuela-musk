


import random
from collections import deque

def sensor_datos():
    parar = True
    contador = 0
    while parar == True:
        temperatura = int(random.random() * 100)
        humedad = int(random.random() * 100)
        tiempo = {
            "Temperatura" : temperatura,
            "Humedad" : humedad
        }
        yield tiempo
        # contador += 1
        # if(contador == 2120): #* "1 Minuto"
        #     parar = False



def filtrar_datos(toda_info):
    contador = 0
    for i in toda_info:
        contador += 1
        if((1 <= i["Temperatura"] <= 50) and (0 <= i["Humedad"] <= 100)):
            datos_tiempo_guardado = {
                "Temperatura" : i["Temperatura"],
                "Humedad" : i["Humedad"]
            }
            yield datos_tiempo_guardado
    

# * Se hará un promedio de 15 de la lectura
promedio = 15

def recopilacion_info(filtrado_datos):
    promedios_numero_temperatura = []
    promedios_numero_humedad = []
    promedios_numero_temperatura = deque(maxlen = promedio)
    promedios_numero_humedad = deque(maxlen = promedio)
    for i in filtrado_datos:
        promedios_numero_temperatura.append(i["Temperatura"])
        promedios_numero_humedad.append(i["Humedad"])
        guardar_promedios = {
            "Temperatura" : int(sum(promedios_numero_temperatura) / len(promedios_numero_temperatura)),
            "Humedad" : int(sum(promedios_numero_humedad) / len(promedios_numero_humedad))
        }
        yield guardar_promedios




def mostrar_promedios(todos_promedios):
    for i in todos_promedios:
        print(f"Prommedio de 15 de temperatura:  {i["Temperatura"]}, humedad {i["Humedad"]}")

toda_info = sensor_datos()
filtrado_datos = filtrar_datos(toda_info)
todos_promedios = recopilacion_info(filtrado_datos)
print("Estos son todos los promedios de tres valores obtenidos en los 60 segundos")
mostrar_promedios(todos_promedios)


























# import random
# import time
# from collections import deque

# # ==========================================
# # 1. GENERADOR DE LECTURAS (Sensor)
# # ==========================================
# def sensor_datos():
#     pausado = False
#     # El ejercicio pide lecturas infinitas
#     while True:
#         temperatura = int(random.random() * 100)
#         humedad = int(random.random() * 100)
#         tiempo = {"Temperatura" : temperatura, "Humedad" : humedad}
        
#         # SI ESTÁ PAUSADO devuelve None, si no, devuelve el tiempo.
#         # Al poner 'orden = yield ...', guardamos lo que nos envíen con .send()
#         orden = yield (tiempo if not pausado else None)
        
#         # Procesamos la orden que entra por el .send()
#         if orden == "pausa":
#             pausado = True
#             print("\n[SENSOR] -> Comando 'pausa' recibido. Frenando...")
#         elif orden == "reanudar":
#             pausado = False
#             print("\n[SENSOR] -> Comando 'reanudar' recibido. Arrancando...")

# # ==========================================
# # 2. GENERADOR DE FILTRADO
# # ==========================================
# def filtrar_datos(toda_info):
#     next(toda_info) # Arrancamos el sensor para que espere en el yield
#     orden = "continuar"
    
#     while True:
#         # En vez de un 'for', le pedimos el dato al sensor usando .send()
#         i = toda_info.send(orden)
        
#         if i is None:
#             orden = yield None
#             continue
            
#         if (1 <= i["Temperatura"] <= 50) and (0 <= i["Humedad"] <= 100):
#             datos_tiempo_guardado = {
#                 "Temperatura" : i["Temperatura"],
#                 "Humedad" : i["Humedad"]
#             }
#             # Devolvemos el dato y capturamos la siguiente orden del sistema
#             orden = yield datos_tiempo_guardado
#         else:
#             # Si el dato no es válido, ignoramos y le pedimos otro inmediatamente
#             orden = "continuar"

# # ==========================================
# # 3. PROMEDIO MÓVIL
# # ==========================================
# promedio = 15

# def recopilacion_info(filtrado_datos):
#     next(filtrado_datos) # Arrancamos el filtro
#     promedios_numero_temperatura = deque(maxlen = promedio)
#     promedios_numero_humedad = deque(maxlen = promedio)
#     orden = "continuar"
    
#     while True:
#         # Le pedimos el dato filtrado al paso anterior usando .send()
#         i = filtrado_datos.send(orden)
        
#         if i is None:
#             orden = yield None
#             continue
            
#         promedios_numero_temperatura.append(i["Temperatura"])
#         promedios_numero_humedad.append(i["Humedad"])
        
#         guardar_promedios = {
#             "Temperatura" : int(sum(promedios_numero_temperatura) / len(promedios_numero_temperatura)),
#             "Humedad" : int(sum(promedios_numero_humedad) / len(promedios_numero_humedad))
#         }
#         # Devolvemos los promedios y capturamos la orden
#         orden = yield guardar_promedios

# # ==========================================
# # 4. EJECUCIÓN Y CONTROL DINÁMICO
# # ==========================================
# toda_info = sensor_datos()
# filtrado_datos = filtrar_datos(toda_info)
# todos_promedios = recopilacion_info(filtrado_datos)

# next(todos_promedios) # Arrancamos el motor final

# print("--- Iniciando sistema. Se pausará en el ciclo 5 y reanudará en el 10 ---")
# accion_usuario = "continuar"

# for ciclo in range(1, 16):
#     # Simulamos órdenes interactivas del usuario usando los ciclos
#     if ciclo == 5:
#         accion_usuario = "pausa"
#     elif ciclo == 10:
#         accion_usuario = "reanudar"
#     elif ciclo > 10:
#         accion_usuario = "continuar"
        
#     # AQUÍ SE USA EL .SEND() QUE PIDE EL EJERCICIO
#     i = todos_promedios.send(accion_usuario)
    
#     if i is not None:
#         print(f"Ciclo {ciclo:02d} -> Promedio de 15 de temperatura: {i['Temperatura']}, humedad {i['Humedad']}")
#     else:
#         print(f"Ciclo {ciclo:02d} -> [Sistema en pausa... esperando reanudación]")
        
#     time.sleep(0.4)
