


# ! Este ejercicio está más enfocado a la realización de un sensor que recoge temperaturas de 3 blog distintos y te da una media

# ! Creamos los objetos de temperatura de diferentes web (haciendo web scraping)
from datetime import datetime
import random



# * Aquí estará los datos exactos, como la ciudad o dirección del viento o la fecha actual


def sensores_datos():
    paginas_web = ["El Mundo", "El Tiempo", "ABC"]
    localizacion = "Huelva"
    direccion_viento = "Norte"
    parar = True
    
    while parar == True:
        
        for i in range(len(paginas_web)):
            lectura_datos = {
                    "Localizacion" : localizacion,
                    "Fecha" : datetime.now(),
                    "Temperatura": random.randint(-10,60),
                    "Viento" : random.randint(0,40),
                    "Direccion Viento": direccion_viento,
                    "Precipitaciones" : round(random.random(),2),
                    "Humedad" : random.randint(0,120)
                }
            yield paginas_web[i], lectura_datos

        parar_while = input(str("Quieres parar de recibir datos pulsa 1 para SI o 2 o intro para NO ")).lower() 
        if(parar_while == "1"):
            parar = False

todos_datos = sensores_datos()


# * Guardo todos los datos de forma ramdom que me aparecen para realizar el promedio
temperatura = []
media_temperatura = 0
viento = []
media_velocidad_viento = 0
precipitaciones = []
media_porcentaje_precipitaciones = 0
humedad = []
media_humedad = 0


for i in todos_datos:
    temperatura.append(i[1]["Temperatura"])
    media_temperatura = round(sum(temperatura) / len(temperatura),2)
    viento.append(i[1]["Viento"])
    media_velocidad_viento = round(sum(viento) / len(viento),2)
    precipitaciones.append(i[1]["Precipitaciones"])
    media_porcentaje_precipitaciones = round(sum(precipitaciones) / len(precipitaciones),2)
    humedad.append(i[1]["Humedad"])
    media_humedad = round(sum(humedad) / len(humedad),2)



