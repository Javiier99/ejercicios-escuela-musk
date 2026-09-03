class MiApp:
    def __init__(self):
        self.rutas = {}  # url -> función

    def route(self, path):
        def decorador(func):
            self.rutas[path] = func  # registro
            return func              # la función vuelve intacta
        return decorador

    def ejecutar(self, path):
        if path in self.rutas:
            return self.rutaspath
        return "404 Not Found"


app = MiApp()

@app.route('/saludo')
def saludo():
    return "Hola"

@app.route('/adios')
def despedida():
    return "Chao"

