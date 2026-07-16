# En algunos ejercicios que he pesnado en resolverlos de otra forma, los he colocado resueltos en formas diferentes

#? 1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!”.

# Primera forma

print("Buenos días a todo el mundo!")

# Segunda forma

mensaje = "Buenos días a todo el mundo!"
print(mensaje)

# Tercerra forma

def saludar():
    mensaje = "Buenos días a todo el mundo!"
    print(mensaje)

saludar()


#? 2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.

a = "¿Como estás?"
b = "mundo,"
c = "Hola"

print(c,b,a)


#? 3. Haz un programa que declare dos números y que escriba la suma.

numero1 = 10
numero2 = 3
numero3 = numero1 + numero2

print(f'El resultado de la suma {numero1} + {numero2} es: {numero3}')


#? 4. Haz un programa que declare dos números y que escriba el máximo.

numero1 = 20
numero2 = 19

if(numero1 > numero2):
    print(f'El número {numero1} es el mayor de los dos números')
elif(numero2 > numero1):
    print(f'El número {numero2} es el mayor de los dos números')
else:
    print(f'Ambos números {numero1} y {numero2} son iguales')



#? 5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.


numero = 20
numero2 = 22
numero3 = 21

print('El número más grande entre {}, {} y {} es {}'.format(numero, numero2, numero3, max(numero,numero2,numero3))) # El max() lo he puesto ahi para probar si funciona o hay que hacerlo fuera del print


#? 6. Hacer un programa que dado un valor calcule su cuadrado y el cubo. 

valor = 10

print(f'El calculo al cuadrado del valor {valor} es {valor**2} y el calculo al cubo es {valor**3}')



#? 7. Haz un programa que devuelva el valor absoluto de un número.

numero = -10.23

print(abs(numero))


# Otra forma
if numero < 0:
    print(f'El valor absoluto de {numero} es {-numero}')
else:
    print(f'El valor absoluto de {numero} es {numero}')




#? 8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a entre b. Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2

# 0 ≤ r < b y d · b + r = a
# 0 ≤ 2 < 5 y 6 · 5 + 2 = 32


#* colocar cualquier numero 

a = int(input("Introduce un número natural no puede ser decimal: ")) #* Aquí debe de ir un input para que el usuario coloque un número
b = int(input("Introduce un número natural no puede ser decimal: ")) #* Aquí debe de ir un input para que el usuario coloque un número

#* División entera y residuo
d = a // b
r = a % b

print(f'La división entera de {a} entre {b} es: {d} y el residuo es: {r}, lo cual cumple con la condición 0 ≤ {r} < {b} y {d} · {b} + {r} = {a}')


#?? 9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.

segundos = int(input("Introduce una cantidad de segundos: ")) #* Colocamos los segundos que vamos a calcular

minutos = int(segundos // 60)
horas = int(minutos // 60)
dias = int(horas // 24)
segundos_restantes = int(segundos % 60)
minutos_restantes = int(minutos % 60)

print(f"La cantidad de segundos escogida es: {segundos} lo cual en minutos son {minutos} y en horas son {horas} que equivale a {dias} días. Además, a tener en cuenta los resudios de minutos: {minutos_restantes} y los segundos restantes: {segundos_restantes} ")


#? 10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. (F= 1.8C + 32 y  ºK =°C + 273ºK).


temperaturaCelsius = float(input("¿Qué temperatura en grados Celsius hace? "))
temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32
temperaturaKelvin = temperaturaCelsius + 273.15

print(f'La temperatura de {temperaturaCelsius}ºC equivale a {temperaturaFahrenheit}ºF y a {temperaturaKelvin}ºK')


# Ejercicios tema 3

#? 1. Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima.


numeroDecimal = float(input("Introduce un número decimal: ")) #* Aquí debe de ir un input para que el usuario coloque un número decimal
transformarNumeroEntero = int(numeroDecimal)

print(f'El numero entero es {transformarNumeroEntero}')


#? 2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.

numeroDecimal = float(input("Introduce un número decimal: ")) #* Aquí debe de ir un input para que el usuario coloque un número decimal
numeroRedondeado = round(numeroDecimal)
numeroTipo = type(numeroDecimal)


print(f'El tipo del número es {numeroTipo} y su valor redondeado es {numeroRedondeado}')


#? 3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
diferencia = abs(numero1 - numero2)

print(f'La diferencia en valor absoluto es: {diferencia}')





