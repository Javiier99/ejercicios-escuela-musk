
import time

def login(func):
    def wrapper(usuario, contraseña):
        print("Entrando, por favor espere...")
        time.sleep(1.2)
        print(f"Has entrado en tu sesión {usuario}")
        return func(usuario, contraseña)
    return wrapper

def autenticacion(func):
    def wrapper(usuario, contraseña):
        print("Accediento al sistema y comprobando si el usuario y contraseña es correcto")
        if(usuario == "Javier" and contraseña == 123):
            print("El usuario es correcto")
            return func(usuario, contraseña)
        else:
            print("El usuario es incorrecto")
    return wrapper

def tiempo(func):
    def wrapper(usuario, contraseña):
        inicio = time.time()
        time.sleep(1.2)
        fin = time.time()
        resultado_tiempo =  float(fin - inicio)
        resultado_tiempo = round(resultado_tiempo,2)
        print(f"El programa ha tardado {resultado_tiempo} segundos")
        return  func(usuario, contraseña)
    return wrapper



@autenticacion
@tiempo
@login
def procesar_datos(usuario, contraseña):
    return usuario, contraseña

procesar_datos("Javier", 123)



