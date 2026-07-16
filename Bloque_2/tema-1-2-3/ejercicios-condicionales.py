#TODO: Ejercicios de condicionales de phyton
#* Nivel Básico
#? Mayor de edad: Pide al usuario su edad e indica si es mayor o menor de edad

edad = int(input('¿Cuál es tu edad?'))  

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")


#? Número positivo o negativo: Pide un número e indica si es positivo, negativo o cero.

numero = int(input('Dame un número: '))

if numero > 0:
    print('El numero es positivo')
elif numero < 0:
    print("El numero es negativo")
elif numero == 0:
    print("El numero es cero")


#? Contraseña simple: Pide al usuario que escriba una palabra. Si coincide con 'python', muestra 'Acceso concedido'. En caso contrario, 'Acceso denegado'

usuario = "javier"
contraseña = "python"

usuarioCliente = (input('Introduce tu usuario: ')).lower()
contraseñaCliente = (input("Introduce tu contraseña: ")).lower()

if (usuarioCliente == usuario) and (contraseñaCliente == contraseña):
    print("Acceso concedido")
elif usuarioCliente != usuario:
    print("Usuario Incorrecto")
elif contraseñaCliente != contraseña:
    print("Contraseña Incorrecta")
else:
    print("Acceso denegado")




#* Nivel Medio

#? Descuento en tienda: Pide el precio de un producto. Si cuesta más de 100€, aplica un 10% de descuento. Si no, no aplica descuento. Muestra el precio final

precioProducto = float(input('Introduce el precio del producto: '))
precioFinal = 0

if precioProducto >= 100:
    descuentoProducto = precioProducto *  0.10
    precioFinal = precioProducto - descuentoProducto
    print(f'El precio del producto final con descuento del 10% es: {precioFinal}€ te has ahorrado {descuentoProducto}€')
else:
    precioFinal = precioProducto
    print(f'En este caso no se aplicaría ningún descuento, el precio final del producto es: {precioFinal}€')




#? Calificación académica: Pide una nota (0 a 10). Según el rango, muestra Suspenso, Aprobado, Notable o Sobresaliente.


notaAlumno = float(input('Introduce tu nota: '))

if notaAlumno <= 10 and notaAlumno >= 0:

    match notaAlumno:
        case 0 | 1 | 2 | 3 | 4:
            print('Estás suspendido')
        case 5 | 6:
            print('Has aprobado')
        case 7 | 8: 
            print('Has sacado notable')
        case 9 | 10: 
            print('Has sacado sobresaliente')
else:
    print('Has introducido una nota no válida, introduce otra nota')






#? Par o impar y múltiplo de 5: Pide un número y determina si es par o impar, y además si es múltiplo de 5.

numero = int(input("Escoge un número sin decimales: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
elif numero % 2 != 0 and numero % 5 == 0:
    print(f"El número {numero} es impar y es multiplo de 5")
elif numero % 2 != 0:
    print(f"El número {numero} es impar ")
else:
    print("Escoge un número")



#* Nivel Avanzado


#? Cine con descuento especial: Pide la edad y si tiene carnet de estudiante. Según las condiciones, aplica diferentes descuentos.


edad = int(input("¿Cual es tu edad? "))
carnetEstudiante = input("¿Tienes carnet de estudiante? (si/no) ").lower()


if (edad < 14 and carnetEstudiante == "no") or (carnetEstudiante == "si" and edad < 14):
    print("Llama a tus padres")
elif carnetEstudiante == "si" and edad < 25 :
    print("Tienes un descuento del 20% en la entrada de cine")
elif carnetEstudiante == "si" and edad >= 25:
    print("Tienes un descuento del 10% en la entrada de cine")
elif carnetEstudiante == "no" and edad < 25:
    print("Tienes un descuento del 10% en la entrada de cine")
elif carnetEstudiante == "no" and edad >= 25:
    print("No tienes ningún descuento en la entrada de cine")
else: 
    print("Has introducido una edad o respuesta no valida")




#? Juego de adivinanza: El programa guarda un número fijo. El usuario escribe un número. Indica si ha acertado o si el número secreto es mayor o menor.


numeroPrograma = 7
numeroUsuario = 0
parar = False


while parar == False:
    numeroUsuario = int(input('Escoge un número del 1 al 10: '))

    if numeroUsuario == numeroPrograma:
        print("¡Has acertado el número secreto!")
        parar = True
    elif (numeroUsuario < numeroPrograma):
        print(f'El numero secreto es mayor que {numeroUsuario}')
    elif (numeroUsuario > numeroPrograma):
        print(f'El numero secreto es menor que {numeroUsuario}')
    else: 
        print("Has introducido un número no válido, por favor introduce un número del 1 al 10")





#? Clasificador de triángulos: Pide tres lados. Clasifica como equilátero, isósceles o escaleno.

#* Primero realizo la pregunta para saber los lados de los triangulos

triangulo = [0, 0, 0]

trianguloCalculo = 0

for i in range(3):
    triangulo[i] = int(input(f"Cuanto mide el lado {i + 1}: "))

# * Segundo, ahora verifico para poder dividir entre los disintos triangulos

trianguloEquilatero = list(set(triangulo)) #* Para que sea equilatero, con que le meta set y me diga que solo quede un elemento es suficiente ya que solo quedará 1 y conque lo cuente cuantos elementos hay en la lista con len() lo tendría


if len(trianguloEquilatero) == 1: #* Al principio probé haciendo un calculo con la idea de que si todos son iguales, lo divides entre 3, el residuo es 0, hasta que probé 1, 2, 3.... En definitiva, todo multiplo de 3, daba triangulo equilatero
    print('El triangulo es equilatero')
else: 
    # * Para el triangulo Isosele y escaleno hay que verificar más PDT: Esta era la versión antes de que me diera cuenta que puedo hacer lo mismo que he realizado en triangulo equilatero
    if (triangulo[0] == triangulo[1]):
        print("El triangulo es Isosele por los lados 1 y 2")
    elif(triangulo[0] == triangulo[2]):
        print("El triangulo es Isosele por los lados 1 y 3")
    elif(triangulo[2] == triangulo[2]):
        print("El triangulo es isosele por los lados 2 y 3")
    else:
        print("El triangulo es escaleno")




# * Versión mejorada

saberTriangulo = list(set(triangulo))

if (len(saberTriangulo) == 1):
    print("El triangulo es equilatero")
elif(len(saberTriangulo) == 2):
    print("El triangulo es isosele")
elif(len(saberTriangulo) == 3):
    print("El triangulo es escaleno")









# TODO: Ejercicios de la vida real

#? 1) Corregir un error lógico - Código original (el alumno debe corregir el tipo y la comparación):

# * Código facilitado
edad = input("Introduce tu edad: ")
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")




# * Código mejorado
# * Añadido, un nombre para relacionar la edad con la persona(se debería añadir DNI en su caso), un int() en la edad para que nos dé un número

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print(f"Hola {nombre}! Eres mayor de edad ....")
else:
    print(f"Hola {nombre}! Eres menor de edad ....")




#? 2) Optimizar condicionales repetidos Código original (el alumno debe simplificar los if/else anidados):

#  * Código facilitado

color = input("Escribe un color: ")
if color == "rojo":
    print("Color válido")
else:
    if color == "azul":
        print("Color válido")
    else:
        if color == "verde":
            print("Color válido")
        else:
            print("Color no válido")

# * Código mejorado
# * Está puesto como función ya que puede dar la cuestión de que ese mismo código se reutilice en otro punto

color = str(input("Escribe un color: ")).lower()

todosColores = ["rojo", "azul", "verde", "amarillo", "negro"]

def colorValido(color):
    print(f"El color {color}, Es un color valido")

if(color in todosColores):
    colorValido(color)
else:
    print("No has escogido un color, vuelve a hacerlo")




# ? 3) Añadir nuevas categorías a un código existente -- Código original (el alumno debe modificarlo para incluir 'Notable' y 'Sobresaliente'):

#  * Código facilitado

nota = int(input("Introduce tu nota: "))
if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")




# * Código mejorado

nombre = str(input("Introduce tu nombre "))
nota = int(input("Introduce tu nota: "))


if(0 <= nota <= 10):
    match nota: 
        case 1 | 2 | 3 | 4:
            print(f"Hola {nombre} tienes que hacer la recuperación, tu nota es un {nota}")

        case 5 | 6:
            print(f"Hola {nombre} has aprobado, tu nota es un {nota}")
        
        case 7 | 8:
            print(f"Hola {nombre}, tu nota es un {nota} muy bien!")

        case 9 | 10:
            print(f"Hola {nombre}, tu nota es un {nota} un sobresaliente!")










