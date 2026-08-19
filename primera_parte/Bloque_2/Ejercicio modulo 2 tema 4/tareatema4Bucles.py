
# 1 Ejercicio tema 3

# ? Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.

a = 0
b = 0
bucleFuncion = False

def volverAEscrivirNumero(a,b,bucleFuncion):
    a = int(input("Escribe un 1º número: "))
    b = int(input("Escribe un 2º número: "))
    if(bucleFuncion == True):
        calculoNumero(a,b,bucleFuncion)
    return(a,b, bucleFuncion)


a,b,bucleFuncion = volverAEscrivirNumero(a,b,bucleFuncion)

def calculoNumero(a,b, bucleFuncion):

    if(a < b):
        print(a)
        while a and b:
            a += 1
            print(a)
            if(a == b):
                break
    elif(a > b):
        print(a)
        while a and b:
            a -= 1
            print(a)
            if(a == b):
                break
    elif(a == b):
        print("Vuelve a escribir dos números, que no sean iguales")
        bucleFuncion = True #Si quito esto, el bucle no funciona
        volverAEscrivirNumero(a,b,bucleFuncion)
        

calculoNumero(a,b, bucleFuncion)



# ? 2. Haz un programa que lea una secuencia de 10 números y que escriba la media.

listaNumeros = []

for i in range(1, 11):
    numero = int(input(f"Dime el número en la posición {i}: "))
    listaNumeros.append(numero)


media = len(listaNumeros)

print("La media de los números es: ", (sum(listaNumeros))/media)


# ? 3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.



tamañoLista = int(input("¿Qué tamaño será la lista? Escoge un número: "))

for i in range(tamañoLista):
    numeros = int(input("Selecciona los números correspondientes que quieres añadir a la lista: "))
    par = numeros % 2
    if(par == 0):
        print(f"El primer número par es {numeros} en la posición {i+1}")
        break



#? 4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.


n = int(input("Dime un número: "))
parar = False

valorMultiplicar = 0

while(parar == False):
    resultado = valorMultiplicar * n
    print(f'{n} x {valorMultiplicar} = {resultado}')
    if(valorMultiplicar == 10):
        parar = True
    valorMultiplicar += 1



#? 5. Haz un programa que lea un número y que lo escriba del revés.

# * Una forma
numero = int(input("Di un número "))

numeroAlReves = ''


while numero > 0:
    numeroAlReves += str(numero % 10) 
    numero = numero // 10

print(numeroAlReves)



# * Otra forma
numeroString = str(input("Di un número: "))

numeroSeparado = list(numeroString)


for i in reversed(numeroSeparado):
    print(i, end="")



# ? 6. Haz un programa que lea un número y que escriba el número de dígitos.


# * Sin usar ningún bucle

numeroString = str(input("Di un número: "))

numeroSeparado = list(numeroString)

contadorDeNumero = len(numeroSeparado)

print(f'El numero {numeroString} posee {contadorDeNumero} digitos')



# * Usando bucles


numero = str(input("Dame un número: "))
listaNumero = list(numero)
for i in range(len(listaNumero)+1):
    print(i)
    if(i == len(listaNumero)):
        print(f"El número {numero} tiene {i} digitos")








# ? 7. Haz un programa que diga si un natural n es capicua o no.

numero = int(input("Di un número "))
numeroGuardar = numero
numeroComprobar = str(numero)

numeroAlReves = ''

while numero > 0:
    numeroAlReves += str(numero % 10) 
    numero = numero // 10

if(numeroAlReves == numeroComprobar):
    print(f'El número {numeroGuardar} es capicua')
else:
    print(f'El número {numeroGuardar} no es capicua')





#? 8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.

# * Sin bucles

años = int(input("Introduce un año: "))


if((años >= 1900) and (años <= 2000)):
    print(f"El año {años} pertenece al siglo XX")
else:
    print(f"El año {años} NO pertenece al siglo XX")



# * Con bucles

años = int(input("Introduce un año: ")) 
contador = 0

while años !=  0:
    calculoAño = años // 100
    if((calculoAño + 1) == 20):
        contador += 1
    años = int(input("Introduce un año: ")) 

print(f"Pertenecen {contador} años al siglo XX")






# ? 9. Haz un programa que reciba una secuencia de naturales de tamaño n y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.


numeroBucle =int(input("Pon cuantos números quieres poner "))

numeros = 0
numerosString = ''
guardarPrimerNumero = False
primerNumero = 0
pasamosSiguientePaso = False

for i in range(numeroBucle):
    numeros  = int(input("Empieza a colocar números "))
    numerosString += str(numeros)
    if(guardarPrimerNumero == False):
        primerNumero = numeros
        guardarPrimerNumero = True


for i in range(1,len(list(numerosString))):
    numeroAcomprobar = int(list(numerosString)[i])
    if(primerNumero > numeroAcomprobar):
        print(f"El primer número que es inferior al {primerNumero} es {numeroAcomprobar}")
        break



#? 10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.



numero = int(input("Dame numeros, el 0 finaliza el bucle: "))


contador = 0

while numero != 0:
    contador += 1
    numero = int(input("Dame numeros, el 0 finaliza el bucle: "))

print(f"Has introducido un numero de {contador} cifras")




# ? 11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.



temperaturas = int(input("Dime temperaturas, coloca 1000 para finalizar: "))
strTemperaturas = ''


TemperaturaA = 0

while temperaturas != 1000:
    strTemperaturas += str(f"{temperaturas}, " )
    if(temperaturas > TemperaturaA):
        TemperaturaA = temperaturas
        print(TemperaturaA)
    temperaturas = int(input("Dime temperaturas, coloca 1000 para finalizar: "))

print(f"De las temperaturas dichas, {strTemperaturas}la más alta es: {TemperaturaA}")



# ? 12. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50.



numero = int(input("Dime un número, usa el 0 para finalizar: "))
noSupera50Str = ''
contadorNoSupera50 = 0
supera50Str = ''
contadorSupera50 = 0

while numero != 0:
    
    if(numero > 50):
        supera50Str += str(f"{numero}, ")
        contadorSupera50 += 1
    elif(numero < 50):
        noSupera50Str += str(f"{numero}, ")
        contadorNoSupera50 += 1
    numero = int(input("Dime un número, usa el 0 para finalizar: "))

print(f"De los números que has aportado, estos números {supera50Str}superan los 50, solo hay {contadorNoSupera50} que NO superan los 50: {noSupera50Str}estos números, no lo superan")




#? 13. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50 y que no hay más de tres que superen 40.

numero = int(input("Dame numeros, el 0 finaliza el programa: "))
supera50 = 0
supera40 = 0

while 0 != numero:
    if(numero > 50):
        supera50 += 1
        if(supera50 > 50):
            supera50 += 1
            print("Hay un valor que ha superado los 50")
            numero = 0
            break
    if(numero > 40):
        supera40 += 1
        if(supera50 != 1):
            match supera40:
                case 1:
                    print(f"Has superado el numero 40: {supera40} vez")
                case 2:
                    print(f"Has superado el numero 40: {supera40} veces")
                case 3:
                    print(f"Has superado los 30 el maximo permitido {supera40} veces")
                    numero = 0
                    break
        elif(supera50 == 1):
            numero = 0
            break
    numero = int(input("Dame numeros, el 0 finaliza el programa: "))


if(supera50 == 1 and supera40 != 0):
    print(f'Has seleccionado un número que supera los 50 y por lo tanto finaliza el programa, y {supera40} que supera los 40.')
elif(supera50 != 1 and supera40 != 0):
    print(f"Ningún número supera los 50 y {supera40} que superan los 40 por lo tanto finaliza el programa ")
elif(supera50 != 1 and supera40 == 0):
    print("Ningún número supera los 50, y además ningún numero super los 40")




# ? 14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.



numero = int(input("Dame números positivos o negativos, 0 para finalizar el programa "))
numeroPositivo = 0
numeroNegativo = 0

while numero != 0:
    if(numero < 0):
        numeroNegativo += 1
    elif(numero > 0):
        numeroPositivo += 1
    numero = int(input("Dame números positivos o negativos, 0 para finalizar el programa "))


if(numeroPositivo < numeroNegativo):
    print("Hay más numeros negativos")
elif(numeroPositivo > numeroNegativo):
    print("Hay más numeros positivos")
else:
    print("Hay numeros iguales tanto positivos como negativos")



# ? 15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuál es el número que hay antes de primer negativo encontrado.


numero = int(input("Dame números, (0 para finalizar el programa) "))

numeroNegativoEncontrado = 0
numerosDados = ''

while numero != 0:
    numerosDados += str(f"{numero}, ")
    if((numero < 0) and (numeroNegativoEncontrado == 0)):
        numeroNegativoEncontrado = numero
    numero = int(input("Dame números, (0 para finalizar el programa) "))

print(f"El primer número negativo encontrado es {numeroNegativoEncontrado} de todos estos números: {numerosDados} que has colocado")



# ? 16. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuántos son múltiples del primero.


multiploPrimero = int(input("Di una serie de números, y te diré si hay multiplos del primero que pongas "))

numero = 1
contador = 0

while numero != 0:
    numero = int(input("Di más números "))
    if((numero % multiploPrimero) == 0 and (numero != 0)):
        contador += 1
        
print(f"Tenemos {contador} multiplos del número que querremos calcular {multiploPrimero}")
    




# ? 17. Haz un programa que lea varias descripciones de rectángulos y de círculos, y que para cada una escriba el área correspondiente. La entrada empieza con un número n, seguido de n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” seguida de dos reales estrictamente positivos que indican la longitud y la anchura. Si es de un círculo, se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.


inicio = "no"

inicio = str(input("Quieres iniciar el Programa Si o No? ")).lower()



areaRectangulo = 0
areaCirculo = 0

while inicio == "si":
    nDescripción = str(input("Es un rectángulo o un círculo el que quieres calcular, pulsa 0 para cerrar el programa: ")).lower()
    if(nDescripción != "0"):
        if((nDescripción == "rectangulo") or (nDescripción == "rectángulo")):
            anchoRectangulo = int(input("Dime el ancho del rectangulo "))
            alturaRectangulo = int(input("Dime el alto del rectangulo "))
            areaRectangulo = anchoRectangulo * alturaRectangulo
            print(f'El área del rectangulo es: {areaRectangulo} m2')
        elif((nDescripción == "circulo") or (nDescripción == "círculo ")):
            radioCirculo = float(input("Dime el radio del circulo "))
            areaCirculo = pow(radioCirculo , 2) * 3.14
            print(f"El área del circulo es: {areaCirculo} m2")
        else:
            print("No le he entendido" )
            continue
    volverCalcular = str(input("Quieres calcular de nuevo un circulo o rectangulo, contesta 'no' si no quieres hacerlo ")).lower()
    if(volverCalcular == "si"):
        continue
    else:
        inicio = "no"


if((areaCirculo != 0) and (areaRectangulo != 0)):
    print(f"El area del circulo final es {areaCirculo} m2 y el area del rectangulo final es {areaRectangulo} m2")
elif((areaCirculo != 0) and (areaRectangulo == 0)):
    print(f"El area del circulo final es {areaCirculo} m2 ")
elif((areaCirculo == 0) and (areaRectangulo != 0)):
    print(f"El area del rectangulo final es {areaRectangulo} m2 ")








# ? 18. Haz un programa que lea un natural n, y que escriba el resultado de la suma siguiente: 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia. 


numeroDeCalculo = int(input("Dime el número de calculos que haremos "))

numero = 0

guardarCalculos = ''

for i in range(numeroDeCalculo):
    numero = pow(i,2) + numero
    guardarCalculos += str(f"+({i})^2")


print(f'El número de secuencia es {numeroDeCalculo} y su calculo es: {guardarCalculos} = {numero}')









