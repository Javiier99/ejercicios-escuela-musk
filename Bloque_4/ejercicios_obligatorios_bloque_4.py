

# ! Ejercicio 1


class Staff():
    def __init__(self, role, depty, salary):
        self.role = role
        self.depty = depty
        self.salary = salary 


class Teacher(Staff):
    def __init__(self, role, depty, salary, name, age):
        super().__init__(role, depty, salary)
        self.name = name
        self.age = age


profesor_1 = Teacher("Teacher", "Math", 1000, "Javier", 30)


print(profesor_1.role)



# ! Ejercicio 2

class Parent_1():
    def __init__(self, x):
        self.x = x

class Parent_2(Parent_1):
    def __init__(self, y, x):
        super().__init__(x)
        self.y = y


class Child(Parent_2):
    def __init__(self, y, x, z):
        super().__init__(y, x)
        self.z = z

prueba = Child("y", "x", "z")

print(prueba.x)
print(prueba.y)
print(prueba.z)



# ! Ejercicio corregido: 

class Parent1:
    def __init__(self, x, **kwargs):
        print('In init method of Parent1')
        self.x = x
        super().__init__(**kwargs)
    def display(self):
        print('In display method of Parent1 x = ', self.x)

class Parent2:
    def __init__(self, y, **kwargs):
        print('In init method of Parent2')
        self.y = y
        super().__init__(**kwargs)
    def display_value(self):
        print('In display method of Parent2 y = ', self.y)

#inheriting both Parent1 and Parent2
class Child(Parent1, Parent2):
    def __init__(self, z, **kwargs):
        print('In init method of Child')
        super().__init__(**kwargs)
        self.z = z

    def display_child(self):
        print('In display method of Child z =', self.z)

obj = Child(x=10, y='Hello', z=20)

obj.display()
obj.display_value()
obj.display_child()
print(Child.mro())











# ! Ejercicio 3


class Vehicle():
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print(f"Detalles del coche: {self.name}, {self.color} y {self.price}")
    
    def max_speed(self):
        print(f"La velocidad máxima del vehículo es: 150km/h")

    def change_grear(self):
        print("Cambio de 6 marchas del vehículo ")

class Car(Vehicle):
    def __init__(self, name, color, price, velocidad, marchas):
        super().__init__(name, color, price)
        self.velocidad = velocidad
        self.marchas = marchas
    
    def max_speed(self):
        print(f"La velocidad máxima del vehículo es: {self.velocidad}km/h")

    def change_grear(self):
        print(f"Cambio de {self.marchas} marchas del vehículo ")


coche1 = Car("Mercedes", "Rojo", 32000, 200, 7)

coche1.max_speed()
coche1.change_grear()









# ! Ejercicio 4



from abc import abstractmethod, ABC

class  BaseClassifier(ABC):
    @abstractmethod
    def preprocess_data(self, data = None, y = None):
        pass
    @abstractmethod
    def fit(self):
        pass
    @abstractmethod
    def  predict(self):
        pass


class SVM(BaseClassifier):
    
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at SVM")
    
    def fit(self):
        print("Training at SVM")

    def  predict(self):
        print("Evaluating at SVM")

class DecisionTree(BaseClassifier):
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at DecisionTree")
    
    def fit(self):
        print("Training at DecisionTree")

    def  predict(self):
        print("Evaluating at DecisionTree")


svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()



# # ! Ejercicio 5


class SVM():
    
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at SVM")
    
    def fit(self):
        print("Training at SVM")

    def  predict(self):
        print("Evaluating at SVM")

class DecisionTree():
    def preprocess_data(self, data = None, y = None):
        print("Preprocessing data at DecisionTree")
    
    def fit(self):
        print("Training at DecisionTree")

    def  predict(self):
        print("Evaluating at DecisionTree")




svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()



# ! Ejercicio 6

from abc import abstractmethod, ABC

class  BaseClassifier(ABC):
    @abstractmethod
    def preprocess_data(self, data = None, y = None):
        pass
    @abstractmethod
    def fit(self):
        pass
    @abstractmethod
    def  predict(self):
        pass

class Algoritmo():
    pass

BaseClassifier.register(Algoritmo)

print(issubclass(Algoritmo, BaseClassifier))



# ! Ejercicio 7

from datetime import datetime
from zoneinfo import ZoneInfo

zona = ZoneInfo("Europe/Madrid")

# 1 Aquí hay un lio, ponenis dias del año, dia del mes y dia de la semana repetido y no se si os referís al dia en cuestión o algo, por lo  que lo tengo individualmente y junto con una fecha normal

# * Fecha y hora actual
fecha_actual = datetime.now(zona)
print(fecha_actual)

# * Año actual

fecha_actual_año_mes_dia = datetime.now(zona).date()
print(fecha_actual_año_mes_dia)


# * Nombre del mes
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fecha_actual_mes = datetime.now(zona).month

print(meses[fecha_actual_mes - 1])


# * Numero de la semana
numero_semana = datetime.now(zona).weekday()

print(numero_semana)

# * Día de la semana

nombre_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero_semana = datetime.now().weekday()

print(nombre_semana[numero_semana])




# ! Ejercicio 8



from datetime import datetime

fecha_input = "Jan 1 2014 2:43PM"

formato = "%b %d %Y %I:%M%p"

fecha_output = datetime.strptime(fecha_input, formato)

print(fecha_output)




# ! Ejercicio 9

from datetime import datetime


hora_actual = datetime.now().hour
min_actual = datetime.now().minute
seg_actual = datetime.now().second

print(f"Ahora son las: {hora_actual}:{min_actual}:{seg_actual}")



# ! Ejercicio 10

from datetime import datetime, timedelta

fecha_actual = datetime.now()
dias_restar = timedelta(days=5) 

hace_cinco_dias = fecha_actual - dias_restar

print(hace_cinco_dias)




# ! Ejercicio 11

from datetime import datetime

fecha_unix_string = "1284105682"
fecha_unix_number = int(fecha_unix_string)

fecha_normal = datetime.fromtimestamp(fecha_unix_number)

print(fecha_normal)


# ! Ejercicio 12


from datetime import datetime, timedelta

hora_actual = datetime.now()

segundos_sumar = timedelta(seconds=5)

resultado = hora_actual + segundos_sumar

print(hora_actual)
print(resultado)






# ! Ejercicio 13

from datetime import datetime

numero_semana = datetime.now().weekday()
print(numero_semana+1) # Se le suma 1 para que sea el número exacto de la semana lo hago el jueves por lo tanto es el 4





# ! Ejercicio 14



from datetime import datetime, timedelta

año_elegido = 2010

fecha_inicio = datetime(año_elegido,1,1).date()
fecha_fin = datetime(año_elegido,12,31).date()

suma_un_dia = timedelta(days=1)
contador_domingos = []
while fecha_inicio <= fecha_fin:
    es_domingo = fecha_inicio.weekday()
    if(es_domingo == 6):
        contador_domingos.append(fecha_inicio)
    fecha_inicio = fecha_inicio + suma_un_dia

print(f"La fecha de los domingos es: ")
for fecha in contador_domingos:
    print(fecha)





# # ! Ejercicio 15

from datetime import datetime, timedelta

fecha_inicio = datetime(2015,1,1).date()
fecha_fin = datetime(2015,12,31).date()

fecha_inicio_formateada = fecha_inicio.strftime("%d/%m/%Y")
fecha_fin_formateada = fecha_fin.strftime("%d/%m/%Y")

suma_un_dia = timedelta(days=1)
contador_lunes = 0
while fecha_inicio <= fecha_fin:
    es_lunes = fecha_inicio.weekday()
    if(es_lunes == 0):
        contador_lunes += 1
    fecha_inicio = fecha_inicio + suma_un_dia

fecha_inicio = fecha_inicio.strftime("%d/%m/%Y")

print(f"Tenemos en total {contador_lunes} lunes desde el dia {fecha_inicio_formateada} al {fecha_fin_formateada} ")



# ! Ejercicio 16

# * Este es el enunciado del ejercicio: Escribe un programa en Python para crear 12 fechas fijas a partir de una fecha especificada en un periodo determinado. La diferencia entre dos fechas será de 20.
# * Dado que no dice si son 20 días, años o meses, lo tomaré como días

from datetime import datetime, timedelta

fecha_escogida = datetime(2020, 11, 2).date()
dias_diferencia = timedelta(days = 20)
guardar_fechas = [fecha_escogida]

for i in range(12):

    fecha_escogida = fecha_escogida + dias_diferencia
    guardar_fechas.append(fecha_escogida)


print("Las fechas incluida la inicial son: ")

print(f"Fecha inicial --> {guardar_fechas[0].strftime("%d/%m/%Y")}")
for fechas in range(1, len(guardar_fechas)):
    print(guardar_fechas[fechas].strftime("%d/%m/%Y"))





# ! Ejercicio 17
# * En este ejercicio lo he realizado de esta forma, porque me pides una función generadora y luego en el dibujo pones un return, por lo que he tirado por la función generadora

from random import random


lista_1 = []
lista_2 = []
lista_3 = []




# * Generamos números aleatorios para nuestras dos listas, de forma aleatoria
for i in range(30):
    numero_lista_1 = int(random() * 100)
    numero_lista_2 = int(random() * 100)
    lista_1.append(numero_lista_1)
    lista_2.append(numero_lista_2)


# * Función generadora:

def generadora():
    i = 0
    try:
        while True:
            numero_lista_3 = lista_1[i] * lista_2[i]
            lista_3.append(numero_lista_3)
            numero_pasado = yield numero_lista_3
            i += 1
    except IndexError:
        pass


numero = generadora()
inicio_generador = next(numero)


def recibir_numeros():
    try:
        while True:
            recibir_numero = numero.send("Número pasado, siguiente número")
            print(recibir_numero)
    except StopIteration:
        print("Se acabó la lista")
recibir_numeros()
print(lista_3)




# ! Ejercicio 18
from random import random

def generador():
    contador = 0
    while contador < 30: # * Pongo 30 vueltas para que pueda frenar en algún punto
        numero_aleatorio = int(random()*100)
        mandar_numero_aleatorio = yield numero_aleatorio
        contador += 1

el_generador = generador()
primer_numero = next(el_generador)
print(primer_numero)

def recibir_generador():
    try:
        while True:
            siguiente_numero = el_generador.send("Se ha pasado el número")
            print(siguiente_numero)

    except StopIteration:
        print("Se acabaron los números")

recibir_generador()



# ! Ejercicio 19


def generador_fibo(n):
    numero_1 = 0
    numero_2 = 1
    contador = 0
    while contador < n:
        yield numero_1
        numero_1, numero_2 = numero_2, numero_1 + numero_2
        contador +=1

fib = generador_fibo(10000)

for i in fib:
    print(i)





# ! Ejercicio 20



n = 10000

def generador(n):
    contador_numero = 0
    while contador_numero <= n:
        numero_por_dos = contador_numero * 2
        yield numero_por_dos
        print("Contador numero", contador_numero)
        contador_numero += 1
        


primer_numero = generador(n)
activar_generador= next(primer_numero)

for i in primer_numero:
    print(i)



# ! Ejercicio 21

# * Aquí en no entiendo las palabras numeros senares, he buscado y me dicen que son números impares, en caso de no ser así, puedo repetir el ejercicio



n = 10000

def generador_numeros_impares():
    contador_impares = 0
    numeros = 0
    parar = True
    while parar == True:
        es_impar = (numeros % 2)

        if(es_impar != 0):
            contador_impares += 1
            yield numeros 

        numeros += 1

        if(contador_impares == n):
            parar = False
            

numeros_impar_generador = generador_numeros_impares()

for i in numeros_impar_generador:
    print("Entra", i)




# ! Ejercicio 22



def error():
    try:
        lista = [1,2,3,4,5]
        for i in range(10):
            print(lista[i])


    except Exception as error:
        tipo_error = error.__class__.__name__
        argumento_error = error.args
        mensaje_error = str(error)

        print("El tipo de error es: ",tipo_error)
        print("El tipo de argumento es: ",argumento_error)
        print("El tipo de mensaje es: ",mensaje_error)

error()



# ! Ejercicio 23


class Negative_Difference_Exception(Exception):
    pass


def calculo(a,b):
    numero = a - b

    if(numero < 0):
        raise Negative_Difference_Exception("Es negativo el númmero")
    else:
        return numero


try:
    calculo(2,4)

except Negative_Difference_Exception as error:
    print("Cuidado el número es negativo") 




# ! Ejercicio 24 
# * Aquí tengo un dilema, osea si pongo el input pero no lo transformo con int dará siempre TypeError y no se si esa es la intención, igualmente lo he puesto aunque no llegue nunca a darse en esta situación

def calculo(a,b):
    a = int(a)
    b = int(b)
    numero = a / b
    return numero

try:
    numero_1 = input("Escoge un número entero ")
    numero_2 = input("Escoge un número entero ")
    resultado = calculo(numero_1, numero_2)

except ZeroDivisionError:
    print("'El divisor no puede ser 0'")

except ValueError:
    print("Los parámetros deben ser número enteros")

except TypeError:
    print("Los parámetros deben ser número enteros")

else:
    print(resultado)





# ! Ejercicio 25

def calculo(a,b):
    a = int(a)
    b = int(b)
    numero = a / b
    return numero

try:
    numero_1 = input("Escoge un número entero ")
    numero_2 = input("Escoge un número entero ")
    resultado = calculo(numero_1, numero_2)

except ZeroDivisionError:
    print("'El divisor no puede ser 0'")

except ValueError:
    print("Los parámetros deben ser número enteros")

except TypeError:
    print("Los parámetros deben ser número enteros")

else:
    print(resultado)

finally:
    print("Esto se ejecuta siempre")






