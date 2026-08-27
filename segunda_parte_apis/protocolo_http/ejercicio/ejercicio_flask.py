
import requests


# * Get

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)




# * POST

def create_new_post(data):
    try:

        create_post = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)
        return f"Se ha creado correctamente el nuevo dato {create_post.status_code}"

    except:
        return "No se ha podido crear, ha ocurrido un problema"


id = int(input("Dime un ID entero: "))
name = str(input("Dame un nombre: "))
body = str(input("Dame un texto: "))

data = {"id" : id, "name" : name, "body" : body}

result = create_new_post(data)

print(result)



# * PUT

def create_new_post(data):
    try:

        update_post = requests.put("https://jsonplaceholder.typicode.com/posts/1", json = data)
        return f"Se ha actualizado correctamente el nuevo dato {update_post.status_code}"

    except:
        return "No se ha podido crear, ha ocurrido un problema"


id = int(input("Dime un ID entero: "))
name = str(input("Dame un nombre: "))
body = str(input("Dame un texto: "))

data = {"id" : id, "name" : name, "body" : body}

result = create_new_post(data)

print(result)



# * PATCH

def create_new_post(data):
    try:

        update_partial_post = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json = {"name" : data})
        return f"Se ha actualizado parcialmente el nuevo dato {update_partial_post.status_code}"

    except:
        return "No se ha podido crear, ha ocurrido un problema"

name = str(input("Dame un nombre: "))

result = create_new_post(name)

print(result)




# * DELETE


def create_new_post(data):
    try:

        update_post = requests.delete("https://jsonplaceholder.typicode.com/posts/1", json = data)
        if(int(update_post.status_code) == 200):
            return f"Se ha borrado correctamente el nuevo dato {update_post.status_code}"

    except:
        return "No se ha podido crear, ha ocurrido un problema"


id = int(input("Dime un ID entero a borrar: "))

data = {"id" : id}

result = create_new_post(data)

print(result)







# * 2



import requests


# 2º Aquí averiguamos ahoroa el tiempo

def weather_today(lat_long):
    try:
        api_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_long[0]}&lon={lat_long[1]}&appid={"1ffeaf866cb171a6076ba91829db4ead"}&lang={"es"}'

    except:
        print("Ha ocurrido un error en obtener el tiempo de la ciudad")

    api_weather_result = requests.get(api_weather, timeout=10)
    api_weather_result_json = api_weather_result.json()
    temp = round( api_weather_result_json['main']['temp'] - 273.15, 2)
    weather = {"Descripcion" : api_weather_result_json['weather'][0]['description'], "Temperatura" : temp}
    return weather



# 1º Saber la latitud y longitud de la ciudad
def lat_and_lon(city):
    try:
        url_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={"1ffeaf866cb171a6076ba91829db4ead"}'
        
    except:
        return "Ha ocurrido un error en la url para obtener la latitud y longitud"

    result_result_city = requests.get(url_city, timeout=80)
    data_city = result_result_city.json()
    lat_long = [data_city[0]['lat'], data_city[0]['lon']]
    result_weather = weather_today(lat_long)
    return f"Actualmente la temperatura de {city} es {result_weather['Temperatura']} grados estándo el tiempo (descripción) en : {result_weather['Descripcion']}"



city = "Aljaraque"
city = str(input("Dime el nombre de una ciudad o pueblo: "))
result = lat_and_lon(city)

print(result)

