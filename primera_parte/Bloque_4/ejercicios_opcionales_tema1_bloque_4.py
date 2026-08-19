
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self.__km = 0
    
    def on(self):
        return f"{self.type} {self._model} se ha encendido"

    def drive(self, km_traveled_user):
        self.km_traveled_user = km_traveled_user
        self.__km = self.km_traveled_user + self.__km

        return f"El usuario ha recorrido {self.km_traveled_user} km"
    def get_kilometraje(self):
        return f"{self.type} {self._brand} modelo {self._model} posee ahora {self.__km} km recorridos"

class Car(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type
    def vehicle_type(self):
        return self.type
    def on(self):
        return f"{self.type} {self._model} se ha encendido metiendo la llave y pisando el embrague"

class Motorbike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type
    def vehicle_type(self):
        return self.type
    def on(self):
        return f"{self.type} {self._model} se ha encendido metiendo la llave y pulsado la maneta del embrague "


moto1 = Motorbike("Kia", "2B", "La Moto")
print(moto1.on())
print(moto1.drive(100))
print(moto1.get_kilometraje())
print(moto1.drive(400))
print(moto1.get_kilometraje())
print("Separador")
coche1 = Car("Opel", "Zafira", "El Coche")
print(coche1.on())
print(coche1.drive(400))
print(coche1.get_kilometraje())
print(coche1.drive(800))
print(coche1.get_kilometraje())