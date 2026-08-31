

# import functools

# def repetir(veces=3):
#     def decorador_real(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(veces):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorador_real

# @repetir(veces=3)
# def saludar(nombre):
#     print("Hola", nombre)

# saludar("Javier")











# import functools

# def repetir(veces=3):
#     def decorador_real(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(veces):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorador_real

# @repetir(veces=3)
# def saludar(nombre):
#     print(f"Hola, {nombre}")

# saludar("Carlos")




import time



def calcularTiempo(funcion):
    def funcionModificada(n):
        inicio = time.time()
        funcion(n)
        final =  time.time()
        print(inicio, final)

    return funcionModificada




@calcularTiempo
def imprimir_numero(n):
    for i in range(n):
        print(i)

imprimir_numero(1000)












def calcularTiempo(n):
    def funcionModificada(n):
        inicio = time.time()
        def imprimir_numero(n):
            for i in range(n):
                print(i)

        imprimir_numero(1000)
        final =  time.time()
        print(inicio, final)

    return funcionModificada


calcularTiempo(1000)


