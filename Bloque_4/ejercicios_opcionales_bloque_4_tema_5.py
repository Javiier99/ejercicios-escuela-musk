





# # # ! Ejercicios de manejo de excepciones en python


# # # * Ejercicio 1


# # a = 10
# # b = 1

# # try:
# #     c = a / b
# # except ZeroDivisionError:
# #     print("No se puede dividir por cero")
# # except TypeError:
# #     print("No puedes dividir un numero por un string")
# # else:
# #     print(c)









# # # * Ejercicio 2


# # numero_usuario = input("Introduce un número: ")

# # try:
# #     numero_usuario = int(numero_usuario)
# # except ValueError:
# #     print("Solo debe de ingresar números")
# # else:
# #     print(numero_usuario)
# # finally:
# #     print("Ha terminado la validación del dato", type(numero_usuario))





# # * Ejercicio 3


# def validar_puntuacion(puntuacion):
    
#     if(1 < puntuacion < 10):
#         pass
#     else:
#         raise ValueError("No está entre 1 y 10")

# try:
#     validar_puntuacion(20)
# except ValueError as error:
#     print("Si no se captura, el programa se detendrá al producirse la excepción.", error)















# def prueba(numero):
#     if(numero < 0):
#         raise ValueError ("El número debe de ser mayor a 0")
#     b = 2 + numero
#     print(b)


# try:
#     prueba(-2)
#     print("Todo exitoso, tiramos pa lante")
# except ValueError as e:
#     print("Tenemos un problema: ", e)


# import io

# nombre_archivo = "Ejemplo"

# try:
#     with open("nombre_archivo") as arhivos:
#         arhivo.write("Hola")
#         10/0
    
#     hola 

# except ZeroDivisionError:
#     print("El programa sigue")

# except io.UnsupportedOperation:
#     print("El programa sigue sin el IO")

# except FileNotFoundError:
#     print("El archivo no existe")

# except Exception as e:
#     print("El archivo no existe", e)
# except SyntaxError as e:
#     print("Seguimos", e)

# print("Prueba de que el programa sigue")









import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_division_normal():
    assert dividir(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)



print(dividir(1, 0))


doblar_numero = 3
def test():
    assert doblar_numero (3)     ==   6



