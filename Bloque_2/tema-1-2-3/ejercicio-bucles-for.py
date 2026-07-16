
# 1 Ejercicios de bucles con python

# 2 Nivel Sencillo

# ? 1. Repetir tu nombre con numeración: Pide al usuario su nombre y muestra 5 veces un mensaje con numeración (1. Hola, Ana...).


# Una primera forma


nombre = str(input("¿Cuál es tu nombre? "))

datosUsuario = ["Hola", nombre, "como", "estás", "hoy"]


for i in range(len(datosUsuario)):
    print(datosUsuario[i])



# Segunda forma


datosUsuario = ["Hola", "null", "como", "estás", "hoy"]

datosUsuario[1] = str(input("Dime tu nombre "))


for i in range(len(datosUsuario)):
    print(datosUsuario[i])



# ? 2. Contar letras de una palabra: Pide una palabra y muestra cada letra en una línea distinta con su posición.

# Una forma

palabra = str(input("Dime una palabra: "))

for i  in range(len(palabra)):
    print(palabra[i])




# ? 3. Cuenta atrás con mensaje final: Muestra los números del 5 al 1 en orden descendente y luego imprime '¡Despegue!'

# * Primera forma

for i in reversed(range(6)):
    print(i)
    if (i == 1):
        print(f"Despegue!")
        break

# * Segunda forma

parar = 6

while parar:
    parar = parar - 1
    print(parar)
    if(parar == 1):
        print(f"Despegue!")
        break




# 2 Nivel Medio


# ? Mostrar múltiplos de 3 hasta 30: Muestra solo los números que sean múltiplos de 3 entre 1 y 30.

# * forma 1

for i in range(31):
    multiplo3 = i % 3
    if(multiplo3 == 0 and i != 0):
        print(f"El numero {i} es multiplo de 3")



# * Forma 2

numero = 1

while numero: 
    multiplo3 = numero % 3
    if(multiplo3 == 0):
        print(f"El numero {numero} es multiplo de 3")
    if(numero >= 30):
        break
    numero = numero + 1



# ? Suma de números del 1 al 10: Calcula la suma total de los números del 1 al 10 usando una variable acumuladora

numero = 0

for i in range(11):
    numero += i
    print(numero)


# ?Contar vocales en una palabra: Pide una palabra y cuenta cuántas vocales tiene recorriendo cada letra con un for

palabra = str(input("Dime una palabra ")).lower()

for i in range(len(palabra)):
    if(palabra[i] == "a" or palabra[i] == "e" or palabra[i] == "i" or palabra[i] == "o" or palabra[i] == "u"):
        print(palabra[i])
    
    if(palabra[i] in "aeiou"):
        print(palabra[i])





# 2 Nivel Avanzado

# ? Tabla de multiplicar: Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10


numero = int(input("Di un número del 1 al 10: "))

for i in range(11):
    print(numero * i)







# ? Contador de letras específicas: Pide una palabra y una letra. Indica cuántas veces aparece esa letra en la palabra


palabra = str(input("Dame una palabra: ")).lower()
letra = str(input("Dame una letra: "))
contadorLetras = 0

for i in range(len(palabra)):

    if(palabra[i] == letra):
        contadorLetras += 1

print(f"Aparecen en la palabra {palabra}, {contadorLetras} veces la letra {letra}")


#? Pirámide de asteriscos: Pide al usuario un número n y muestra una pirámide con n filas (*, **, ***, ...).


numeroAsteriscos = int(input("Dame un número: "))

for i in range(1, numeroAsteriscos + 1):
    print("*" * i)





# 2 Ejercicios de "Vida Real" 



# ? 1) Corregir un error de tipo y cálculo

#* Está realizado para que puedas colocar cualquier número 

numeroBucle = int(input("¿Cuantas veces quieres sumar? ")) 

total = 0
for i in range(1, numeroBucle + 1):
    total += i
    if(numeroBucle == i):
        print("El total es:", total)



# ? Optimizar código repetitivo

# * Código sin optimizar

for i in range(1, 11):
    if i == 1:
        print("1 x 5 =", 5)
    if i == 2:
        print("2 x 5 =", 10)
    if i == 3:
        print("3 x 5 =", 15)
    if i == 4:
        print("4 x 5 =", 20)
    if i == 5:
        print("5 x 5 =", 25)
    if i == 6:
        print("6 x 5 =", 30)
    if i == 7:
        print("7 x 5 =", 35)
    if i == 8:
        print("8 x 5 =", 40)
    if i == 9:
        print("9 x 5 =", 45)
    if i == 10:
        print("10 x 5 =", 50)



#  * Código optimizado

for i in range(1,11):
    print(f"{i} x 5 = {i*5}")


# ? Ampliar funcionalidad

# * Código sin funcionalidad

for i in range(1, 6):
    print(i)


# * Código con funcionalidad
for i in range(1,6):
    if((i % 2) == 0):
        print(i)



































