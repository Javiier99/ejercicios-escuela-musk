
# ! Variables

# ? 1. Haz un programa que lea una secuencia de caracteres acabada en punto y que escriba cuántas letras ‘a’ contiene.


frase = str(input("Introduce una secuencia de caracteres ")).lower()

contador = 0

for i in frase:
    if i == "a":
        contador += 1

print(f"La secuencia contiene {contador} letras 'a'.")


# ? 2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.


frase = str(input("Dame una frase ")).lower()
buscar = str(input("Dime que palabras te busco ")).lower()


contador = frase.count(buscar)

print(f"La palabra {buscar} aparece {contador} veces en la frase: {frase}")


# ? 3. Haz un programa que invierta una cadena dada.


cadena = str(input("Dame una cadena de texto: "))

cadena_reves = "".join(reversed(cadena))

print(cadena_reves)



# * Otra forma sin usar reverse()

cadena = str(input("Dame una cadena de texto: "))
palabras_reves = []

for i in range((len(cadena)-1),-1,-1):
    palabras_reves.append(cadena[i])


print(palabras_reves)
print("".join(palabras_reves))




# ? 4. Haz un programa que divida una cadena en guiones.


cadena = str(input("Dame una cadena de texto con guiones: "))

separar_cadena = cadena.split('-')
cadena_separada = " ".join(separar_cadena)

print(cadena_separada)


# ? 5. Haz un programa que añada una nueva cadena en medio de una cadena dada.



# 1 Primero deberemos de separar la cadena de texto en una lista
cadena = (str(input("Dame una cadena de texto: ")).lower()).split()

# 2 Ahora que tenemos la cadena separada, hay que saber donde colocar la 2º cadena
nueva_cadena = (str(input("Dame la 2º cadena a colocar ")).lower()).split()
colocar_nueva_cadena = str(input("Dime donde quieres colocar la nueva cadena, ten en cuenta que estará detrás de la palabra que escojas: ")).lower()

final_nueva_cadena = []
parar = False

for i in range(len(cadena)):
    if((colocar_nueva_cadena == cadena[i]) and (parar == False)):
        final_nueva_cadena.append(cadena[i])
        for x in range(len(nueva_cadena)):
            # 3 Guardar todo en una nueva cadena en un bucle
            final_nueva_cadena.append(nueva_cadena[x])
            parar = True
    else:
        final_nueva_cadena.append(cadena[i])

print(" ".join(final_nueva_cadena))




#?6. Haz un programa que encuentre la última posición de una subcadena dada.

#* Problema, si se repiten palabras en la misma cadena, cogerá la primera, por eso usando rfind es mejor

cadena_completa = str(input("Introduce la cadena completa: ")).lower()
empieza_cadena_2 = str(input("Dame la palabra la cual empieza la 2º cadena: ")).lower()


numero_cadena = cadena_completa.index(empieza_cadena_2)

segunda_cadena = ""

for i in range(len(cadena_completa)):
    if(numero_cadena <= i):
        segunda_cadena += cadena_completa[i]

print(f"La cadena empieza en el numero {numero_cadena} y la frase de la 2º cadena es: {segunda_cadena}") 


# * Otra forma usando rfind

cadena_completa = str(input("Introduce la cadena completa: ")).lower()
empieza_cadena_2 = str(input("Dame la palabra la cual empieza la 2º cadena: ")).lower()


numero_cadena = cadena_completa.rfind(empieza_cadena_2)

segunda_cadena = ""

for i in range(len(cadena_completa)):
    if(numero_cadena <= i):
        segunda_cadena += cadena_completa[i]

print(f"La cadena empieza en el numero {numero_cadena} y la frase de la 2º cadena es: {segunda_cadena}") 




# ? 7. Haz un programa que elimine cadenas vacías de una lista de cadenas.



cadena = str(input("Dame una cadena de texto: ")).strip().split()
cadena_final ="".join(cadena)

print(cadena_final)



# ? 8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.


# * Como debe de hacerse

import string

texto_no_limpio = "Hola@ c@omo estais"

texto_limpio = texto_no_limpio.translate(str.maketrans("sc","ñq",string.punctuation))


print(texto_limpio)




# * Metodo largo

texto_no_limpio = "H@?¿ola@ ?c@omo&& es¿tai^^s"
caracteres_raros = "@?^&!?¿¡" # * Colocar todos los caracteres que se desea eliminar
caracteres_eliminados = ""
colocar_caracter = ""


for i in range(len(texto_no_limpio)):
    hay_caracter_raro = False
    for x in range(len(caracteres_raros)):
        if(texto_no_limpio[i] == caracteres_raros[x]):
            caracteres_eliminados += caracteres_raros[x]
            hay_caracter_raro = True
        
    if(hay_caracter_raro == False):
        colocar_caracter += texto_no_limpio[i]

print("Texto sin caracteres raros: ", colocar_caracter)
print("Los caracteres eliminados: ", caracteres_eliminados)


# ? 9. Haz un programa que encuentre palabras con letras y números.



cadena_texto = "2H1o2la2 c3o9m7o e9s7tá4s2, 2 H3o6l1a, E2s01toy e9n 8c1las2es d3e py3tho43n"

contiene_numero = "0123456789"

lista_cadena_texto = cadena_texto.split()

cadena_texto_final = ""



for i in range(len(lista_cadena_texto)): # Bucle para dividir de forma individual las listas --> Hola2

    for x in range(len(lista_cadena_texto[i])): # Bucle para dividir por letras/numeros --> H-o-l-a-2

        pasar_letra_1_vez = False
        guardar_palabra_1_vez = False


        # * También ubiese sido posible creo, no hacer otro bucle, si no directamente un if

        for y in range(len(contiene_numero)): #Bucle para comprobar si la palabra contiene algún numero del 0-9

            if((lista_cadena_texto[i][x] != "0") and (lista_cadena_texto[i][x] != "1") and (lista_cadena_texto[i][x] != "2") and (lista_cadena_texto[i][x] != "3") and (lista_cadena_texto[i][x] != "4") and (lista_cadena_texto[i][x] != "5") and (lista_cadena_texto[i][x] != "6") and (lista_cadena_texto[i][x] != "7") and (lista_cadena_texto[i][x] != "8") and (lista_cadena_texto[i][x] != "9") and (pasar_letra_1_vez == False)):
                pasar_letra_1_vez = True
                cadena_texto_final += lista_cadena_texto[i][x]
            elif(lista_cadena_texto[i][x] == contiene_numero[y]):
                break

    cadena_texto_final += " "   


print(cadena_texto_final)



# * Ahora la forma con import string

import string

cadena_texto = "2H1o2la2 c3o9m7o e9s7tá4s2, 2 H3o6l1a, E2s01toy e9n 8c1las2es d3e py3tho43n"


tabla_limpieza = str.maketrans("","", string.digits)

cadena_texto_limpio = cadena_texto.translate(tabla_limpieza)

print(cadena_texto_limpio)



# ? 10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.


import string


cadena_texto = "E^?st^oy es^!t!ud!^ian^[]d_o p-yt?h=o@n"


for i in string.punctuation:
    cadena_texto = cadena_texto.replace(i,"#",-1)

print(cadena_texto)



# ! Listas

#? 1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).

elementos = []

tamaño_secuencia = int(input("Escoge el tamaño de la secuencia con un número: "))

if(tamaño_secuencia > 1):
    for i in range(tamaño_secuencia):
        elementos.append(str(input("Di palabras o elementos: ")))
    print(elementos[1]) # Aquí es donde debe de ir
else:
    print("Error, debes escoger un tamaño de secuencia mayor a 1 ")

# if(tamaño_secuencia > 1):
#     print(elementos[1])


# ? 2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1, y que escriba cuántos son iguales al último.


secuencia_numeros = []

tamaño_bucle = int(input("Dime el tamaño del bucle: "))
contador = 0

for i in range(tamaño_bucle):
    secuencia_numeros.append(int(input("Ve dandome números negativos o positivos ")))
secuencia_numeros.append(-1)

for i in range(len(secuencia_numeros)):
    if(secuencia_numeros[i] == secuencia_numeros[-1]):
        contador += 1

print(f"De la lista que has facilidado, tenemos {contador-1} coincidencias con el -1")


# ? 3. Haz un programa que lea secuencias de enteros acabada en -1, y que escriba cada una invirtiendo la orden de sus elementos.



serie_numeros = []

final_bucle = int(input("Dame una serie de bucles: "))
numero_bucle = 0


while numero_bucle != final_bucle:
    serie_numeros.append(int(input("Dame una serie de números: ")))
    numero_bucle += 1

serie_numeros.append(-1)
serie_numeros.reverse()

print(serie_numeros[1:])


# ? 4. Haz un programa que lea n palabras, y que escriba cada una invirtiendo la orden de sus caracteres.

serie_palabra_invertida = []
serie_palabra = []
numero_palabras = int(input("Dame un número de palabras a colocar: "))

for i in range(numero_palabras):
    palabras = str(input("Dame una serie de palabras: "))
    serie_palabra.append(palabras)
    

serie_palabra.reverse()

for palabra in serie_palabra:
    serie_palabra_invertida.append(palabra[::-1])

print(serie_palabra_invertida)


# ? 5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.

guardar_numeros = []
numeros = int(input("Dime numeros, el 0 es para finalizar: ")) 

while numeros != 0:
    if(numeros > 0):
        guardar_numeros.append(numeros)
    else:
        numeros = int(input("Dime numeros mayores que 0: ")) 
        continue
    numeros = int(input("Dime numeros, el 0 es para finalizar: ")) 


calculo_media = sum(guardar_numeros)/len(guardar_numeros)

print(calculo_media)



# ? 6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos listas de tamaño n y m. Es decir, hay que devolver un vector que tenga los elementos de v1 seguidos de los elementos de v2.


todas_letras_v1 = []
todas_letras_v2 = []
todas_letras_v3 = []

letras_v1 = str(input("Dime letras v1, pulsa 0 para finalizar el bucle: "))

while letras_v1 != "0":
    todas_letras_v1.append(letras_v1)
    letras_v1 = str(input("Dime letras v1, pulsa 0 para finalizar el bucle: "))

print("Ahora vamos la lista v2")

letras_v2 = str(input("Dime letras v1, pulsa 0 para finalizar el bucle: "))
while letras_v2 != "0":
    todas_letras_v2.append(letras_v2)
    letras_v2 = str(input("Dime letras v1, pulsa 0 para finalizar el bucle: "))



for i in range(len(todas_letras_v1)):
    todas_letras_v3.append(todas_letras_v1[i])
for i in range(len(todas_letras_v2)):
    todas_letras_v3.append(todas_letras_v2[i])


print(todas_letras_v3)




# ? 7. Haz un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista_precios = [50, 75, 46, 22, 80, 65, 8]
print(f"El mayor precio es {max(lista_precios)} y el menos es: {min(lista_precios)}")


# ? 8. Haz un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for i in range(len(asignaturas)):
    print(asignaturas[i])


# ? 9. Haz un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros.reverse()
print(len(numeros))
for i in range(len(numeros)):
    if(i == len(numeros)-1):
        mostrar_numeros += f"{numeros[i]}"
    else:
        mostrar_numeros += f"{numeros[i]}, "

print(mostrar_numeros)

# ? 10. Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.

# * Forma 1 sin ver las solucióm

rango_secuencia = int(input("Coloca un rango de secuencia: "))

lista_1 = []
lista_2 = []
lista_3 = []


# * Guardar en zigzag en las listas
guardar_letras = ""
cambiar = False

for i in range(rango_secuencia):
    letras = str(input("Dime letras: "))
    guardar_letras += letras
    if (cambiar == False):
        lista_1.append(letras)
        cambiar = True
    elif (cambiar == True):
        lista_2.append(letras)
        cambiar = False

# * Mostrar dichos cambios alterado


parar = 0


if ((rango_secuencia % 2) == 0):
    # * Esto es si la secuencia es un número par
    while parar == 0:
        if(len(lista_2) != 0):
            lista_3.append(lista_2.pop())
        if(len(lista_1) != 0):
            lista_3.append(lista_1.pop())
        if((len(lista_1) == 0) and (len(lista_2) == 0)):
            parar = 1
            break
else:
    # * Si la secuencia es impar entonces:
    while parar == 0:
        if(len(lista_1) != 0):
            lista_3.append(lista_1.pop())
        if(len(lista_2) != 0):
            lista_3.append(lista_2.pop())
        if((len(lista_1) == 0) and (len(lista_2) == 0)):
            parar = 1
            break


lista_3 = list(reversed(lista_3))

print(lista_3)



# * Forma 2 entendiendo la solución

n = int(input('Introduce cuántos pares de letras vas a poner: '))

v1 = []
v2 = []

# Pedimos los datos en zigzag de forma limpia
for i in range(n):
    letra_a = input('Introduce elemento para Lista 1: ')
    v1.append(letra_a)
    letra_b = input('Introduce elemento para Lista 2: ')
    v2.append(letra_b)

# Los mezclamos directamente
l = []
for i in range(n):
    l.append(v1[i])
    l.append(v2[i])
    
print(f"Resultado final: {l}")



# ? 11. Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos )simultáneamente e imprima sus elementos.

n = int(input("Introduce el tamaño de la primera frecuencias: "))
m = int(input("Introduce el tamaño de la 2º frecuencia: "))
x = []

for i in range(n):
    letra_colocar_1 = str(input("Coloca una letra para la secuencia 1: "))
    x.append(letra_colocar_1)
for i in range(m):
    letra_colocar_2 = str(input("Coloca una letra para la secuencia 2: "))
    x.append(letra_colocar_2)

print("La nueva secuencia es: ", x)


# ? 12. Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] después de un elemento especificado por el usuario. Si el elemento introducido no está presente en la lista debe mostrar el mensaje: 'Elemento no presente en la lista'.

lista = [10, 50, 40, 20, 30]

añadir_elemento = int(input("¿Que número quieres añadir? "))
posicion_a_añadir = int(input(f"¿Después de que numero quieres añadir el {añadir_elemento}? "))

guardar_posicion_numero = 0

for i in range(len(lista)):
    if (lista[i] == posicion_a_añadir):
        guardar_posicion_numero = i + 1
        break

if(guardar_posicion_numero != 0):
    lista.insert(guardar_posicion_numero, añadir_elemento)
    print(lista)
else: 
    print('Elemento no presente en la lista')




# ? 13. Haz un programa que elimine todas las apariciones de un elemento específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].

# * En caso de tener un solo elemento a eliminar:

lista = [10, 50, 40, 20, 60, 30]
elemento_eliminar = int(input("Dime cual es el elemento que quieres eliminar: "))

lista.remove(elemento_eliminar)

print(lista)



# * En caso de tener más de un elemento a eliminar:

lista = [10, 50, 40, 20, 60, 30, 50]
lista_nueva = []

elemento_eliminar = int(input("Dime cual es el elemento que quieres eliminar: "))


for i in lista:
    if(elemento_eliminar != i):
        lista_nueva.append(i)

print(lista_nueva)





# ! Tuplas



# ? 1. Haz una programa que invierta una tupla.

tupla_frutas = ("manzana", "pera", "platano", "cherry", "melón")
tupla_frutas_reverse = ()

for i in range(len(tupla_frutas)-1,-1,-1):
    tupla_frutas_reverse += (tupla_frutas[i],)

print(tupla_frutas_reverse)



# ? 2. Haz un programa que acceda al valor 15 de la tupla.

t1 = ("Naranja", [10, 20, 30], (5, 15, 25))

print(t1[2][1])


# ? 3. Haz un programa que declare una tupla con un solo elemento 10.

numero_1 = (10,)

numero_2 = 10


tupla = (f"{numero_2}",)

print(type(numero_1))
print(type(tupla))


# ? 4. Haz un programa que descomponga la tupla en 4 variables.

tupla = (10, 20, 30, 40)


a, b, c, d = tupla

print(a)
print(b)
print(c)
print(d)


# ? 5. Haz un programa que intercambie dos tuplas en Python.



tupla_1 = (1,2)
tupla_2 = (3,4)

tupla_1, tupla_2 = tupla_2, tupla_1

print(tupla_1)
print(tupla_2)


#? 6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.

tupla_1 = (11, 22, 33, 44, 55, 66)
elementos_copiar_1 = 33
elementos_copiar_2 = 22
tupla_2 = ()

for i in tupla_1:
    if((elementos_copiar_1 == i) or (elementos_copiar_2 == i)):
        tupla_2 += f"{i}",

print(type(tupla_2))


# ?  7. Haz un programa que modifique una tupla.

tupla_1 = [0, 2, 3, [2,3,4], 23]

tupla_1[3][0] = 44

print(tupla_1)


# ? 8. Ordena una tupla de tuplas por el 2º elemento.

tupla_1 = (('a', 23),('b', 37),('c', 11), ('d',29))
lista_temporal = list(tupla_1)
nueva_tupla = ()


hubo_cambio = True

while hubo_cambio:
    hubo_cambio = False
    for i in range(len(lista_temporal) - 1):
        if(lista_temporal[i][1] > lista_temporal[i+1][1]):
            lista_temporal[i], lista_temporal[i+1] = lista_temporal[i+1], lista_temporal[i]
            hubo_cambio = True

nueva_tupla = tuple(lista_temporal)  
print(nueva_tupla)




# ? 9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.


numeros = (50, 10, 60, 70, 50)
contador = 0

for i in numeros:
    if(i == 50):
        contador += 1

print(f"En esa tupla, aparecen {contador} veces el numero 50")



# ? 10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.

numeros = (45, 45, 45, 45)

numeros_iguales = False

for i in range(len(numeros)-1):
    if(numeros[i] != numeros[i + 1]):
        numeros_iguales = True

if(numeros_iguales == False):
    print("Todos los números son iguales")
else:
    print("Los números no son iguales")


# ! Diccionarios

# ? 1. Haz un programa que convierta dos listas en un diccionario.

lista_1 = ['a', 'b', 'c']
lista_2 = [1, 2, 3]


lista_3 = dict(zip(lista_1,lista_2))

print(lista_3)



# ? 2. Haz un programa que fusione dos diccionarios de Python en uno solo.

dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30,}
dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}

dict1.update(dict2)

print(dict1)



#  ? 3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.

datos_escuela = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(f"La nota de historia es: {datos_escuela["class"]["student"]["marks"]["history"]} puntos")


# ? 4. Haz un programa que inicialice el diccionario con valores por defecto.

# * Una forma

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_employees = dict().fromkeys(employees,defaults)

# print(new_employees)

# * 2º Forma

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_employees = {emp: defaults.copy() for emp in employees}

print(new_employees)


# ? 5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}



keys = {}
keys.update({"name" : sample_dict["name"] , "salary" : sample_dict["salary"]})

print(keys)




# ? 6. Haz un programa que elimine una lista de claves de un diccionario.

# * Primera forma
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict.pop("name")
sample_dict.pop("salary")

print(sample_dict)

# * Segunda forma

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

eliminar = ["name", "salary"]

for i in eliminar:
    sample_dict.pop(i)

print(sample_dict)



# ? 7. Haz un programa que compruebe si un valor existe en un diccionario.

diccionario = {'a': 100, 'b': 200, 'c': 300}

comprobar_1 = "a"
comprobar_2 = 100


if (comprobar_1 in diccionario):
    print("Existe")
else:
    print("No existe")

if (comprobar_2 in diccionario.values()):
    print("Existe")
else:
    print("No existe")


# ? 8. Haz un programa que cambie el nombre de la clave de un diccionario.


sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
}

name = list(sample_dict.keys())
value = list(sample_dict.values())
name[3] = "location"
sample_dict = dict(zip(name, value))


# * La mejor forma
sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)




#  ? 9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.

sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# * Una forma
value = list(sample_dict.values())

minimo = min(value)

for materia, nota in sample_dict.items():
    if(minimo == nota):
        print(materia,nota)

# * La forma rápida

print(min(sample_dict, key=sample_dict.get))





# ? 10. Haz un programa que cambie el valor de una clave en un diccionario anidado.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

new_date = 8500

sample_dict['emp3']["salary"] = new_date

print(sample_dict)


# ! Sets

# ? 1. Haz un programa que añada una lista de elementos a un conjunto.



color_1 = {"Yellow", "Orange", "Black"}

color_2 = ["Blue", "Green", "Red"]

color_1.update(color_2)

print(color_1)



#  ? 2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {}

set3 = set1.intersection(set2)

print(set3)




# ? 3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print(set3)



# ? 4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

print(set1.difference(set2))


# ? 5. Haz un programa que elimine elementos del conjunto a la vez.

set1 = {10, 20, 30, 40, 50}

numero_eliminar = {10, 20, 30}

set2 = set1.difference(numero_eliminar)

print(set2)




# ? 6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)

print(set3)



# ? 7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común. En caso afirmativo, mostrar los elementos comunes.

# * primera forma

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}


set3 = set1.intersection(set2)
print(f"El elemento {set3} está en ambos conjuntos")

# * Segunda forma


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set3 = set1.isdisjoint(set2)

if set3 == False:
    print(f"Los conjuntos set1 y set2 comparten al menos un elemento en común")



# ? 8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)

print(set3)



# ! En este ultimo ejercicio hay lio, ya que el enunciado es igual que el numero 8 pero la solución es diferente

# ? 9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos no repetidos.


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)

print(set1)




