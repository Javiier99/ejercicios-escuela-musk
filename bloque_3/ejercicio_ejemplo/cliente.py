


class Cliente():

    def __init__(self, nombre, primer_apellido, telefono, correo):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.telefono = telefono
        self.correo = correo
    
    def mostrar_info(self):
        print(f"El nombre del cliente es {self.nombre} {self.primer_apellido} su forma de contacto es: Teléfono: {self.telefono}, Correo: {self.correo}")

































