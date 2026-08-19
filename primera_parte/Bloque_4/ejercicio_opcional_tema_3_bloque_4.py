
from datetime import datetime, timedelta, time as dt_time
import time
# * Todos los datos necesarios
dia_actual = datetime.now().date()
pedido_recibido = datetime(2026, 6, 19, 2, 33)
pedido_llega_dias_habiles = 22
fecha_estimada_llegada = pedido_recibido + timedelta(days = pedido_llega_dias_habiles)

# * Saber que dia de la semana cae 
dia_semana = fecha_estimada_llegada.isoweekday()

# * En el supuesto caso que caiga en fin de semana, lo pasamos a día laboral
if((dia_semana == 6)):
    fecha_estimada_llegada += timedelta(days=2)
elif((dia_semana == 7)):
    fecha_estimada_llegada += timedelta(days=1)


# * En el supuesto caso que caiga fuera del horario laboral suponiendo que es de 8:00 a 15:00 
# * Suponiendo unos 30 min de margen para sacar camiones y empezar a repartir

limite_inicio = dt_time(9, 00) 
limite_final = dt_time(18, 00)
hora_recibida_pedido = pedido_recibido.time()

if(hora_recibida_pedido > limite_inicio and hora_recibida_pedido < limite_final):
    print(f"Pedido dentro del horario, la fecha de entrega será {fecha_estimada_llegada}")
else:
    
    fecha_estimada_llegada = fecha_estimada_llegada.replace(hour=9, minute=00)
    print(f"El pedido se le entregará el: {fecha_estimada_llegada.day}/{fecha_estimada_llegada.month}/{fecha_estimada_llegada.year} sobre las {fecha_estimada_llegada.hour} horas")



# * Aquí he querido ampliar un poco el ejercicio haciendo que el pedido se entregue a esa hora

# * Bucle

parar = False

while parar == False:
    dia_actual = datetime.now().date()
    ahora_dia_hora = datetime.now()

    if(dia_actual == (fecha_estimada_llegada.date())):
        print(f"El pedido llegará hoy sobre las {fecha_estimada_llegada.hour}")
        parar = True
    
    else:
        dias_faltan = fecha_estimada_llegada.date() - dia_actual
        print(f"Faltan {dias_faltan.days} días para que el pedido se entregue")
        if(dias_faltan > 1):
            print("Falta más de 1 dia")
            time.sleep(43200) # *  12 horas durmiendo el programa para tener un margen
        elif(dias_faltan == 1):
            print("--- ¡AVISO ADELANTADO AL CLIENTE! ---")
            print(f"Mensaje enviado: 'Su pedido llegará MAÑANA a las {fecha_estimada_llegada.hour}:00'")
            para = True # * Avisado al cliente, el bucle ya no hace falta pasariamos a otro bucle más enfocado a los mínutos y horas






















