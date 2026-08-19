


# ? 1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.

secuencia = [5, 7, 3, 4, 2, 1]

def obtener_numeros_pares():
    numero_par = []
    for i in secuencia:
        calculo_numero = i % 2
        if(calculo_numero == 0):
            numero_par.append(i)
    return numero_par

resultado = obtener_numeros_pares()
print(resultado)




# ? 2. Haz un programa que cree una función con longitud variable de argumentos.

func1 = (20, 40, 60, 90)


def funcion(*func1):
    total = 0
    for i in func1:
        total += i
    print(total)

funcion(*func1)



# ? 3. Haz un programa que devuelva múltiples valores desde una función. Crea la función calculaion() de modo que pueda aceptar dos variables y calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una sola llamada.



def calculation(numero1,numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma,resta

resultado = calculation(40,30)
print(f"La suma es {resultado[0]} y la resta es: {resultado[1]}")


# ? 4. Haz un programa que cree una función con un argumento por defecto.
# ? Crea una función show_employee() usando las siguientes condiciones.

# ? -Debe aceptar el nombre y el salario del empleado y mostrar ambos.

# ? -Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.



def show_employee(nombre, salario = 9000):
    print(f"El empleado {nombre} posee un salario de {salario}€")

show_employee("Javier", 10000000)
show_employee("Paco")




# ? 5. Haz un programa que cree una función interna para calcular la suma de la siguiente manera: Crea una función externa que acepte dos parámetros, a y b. Crea una función interna dentro de una función externa que calculará la suma de a y b. Por último, una función externa que sumará 5 en la suma y la devolverá.


def funcion_externa(a,b):
    def funcion_interna(a,b):
        return a + b
    result_funcion_interna = funcion_interna(a,b)
    return result_funcion_interna + 5
    


resultado = funcion_externa(5,10)


print(resultado)




# ? 6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.

import math

numeros = [10, 4, 1, 15]

def calculo(numeros):
    resultado_numeros_al_cuadrado = []
    resultado_numeros_raiz_cuadrado = []
    for i in numeros:
        resultado_numeros_al_cuadrado.append(i **2)
        resultado_numeros_raiz_cuadrado.append(math.sqrt(i))
    return resultado_numeros_al_cuadrado, resultado_numeros_raiz_cuadrado

resultado = calculo(numeros)

print(resultado)






# ? 7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a grande. Por ejemplo, si a =7, b = −3 y c = 1, los valores después de la llamada deben ser a =−3, b = 1 y c = 7.

lista_numeros = [7, -3, 1, 8, 3, 2, 1, 5, -4, -2, -2]
cambio = True

def ordenar_menor_a_mayor(lista_numeros, cambio):
    while cambio == True:
        cambio= False
        for i in range(len(lista_numeros)-1):
            if(lista_numeros[i] > lista_numeros[i+1]):
                lista_numeros[i], lista_numeros[i+1] = lista_numeros[i+1], lista_numeros[i]
                cambio = True



ordenar_menor_a_mayor(lista_numeros, cambio)

print(lista_numeros)



