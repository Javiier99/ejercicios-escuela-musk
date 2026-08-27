
import requests


# # * 1

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
# print(data)




# # * 2

# def create_new_post(data):
#     try:

#         create_post = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)
#         return f"Se ha creado correctamente el nuevo dato {create_post.status_code}"

#     except:
#         return "No se ha podido crear, ha ocurrido un problema"


# id = int(input("Dime un ID entero: "))
# name = str(input("Dame un nombre: "))
# body = str(input("Dame un texto: "))

# data = {"id" : id, "name" : name, "body" : body}

# result = create_new_post(data)

# print(result)



# # * 3

# def create_new_post(data):
#     try:

#         update_post = requests.put("https://jsonplaceholder.typicode.com/posts/1", json = data)
#         return f"Se ha actualizado correctamente el nuevo dato {update_post.status_code}"

#     except:
#         return "No se ha podido crear, ha ocurrido un problema"


# id = int(input("Dime un ID entero: "))
# name = str(input("Dame un nombre: "))
# body = str(input("Dame un texto: "))

# data = {"id" : id, "name" : name, "body" : body}

# result = create_new_post(data)

# print(result)



# # * 4

# def create_new_post(data):
#     try:

#         update_partial_post = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json = {"name" : data})
#         return f"Se ha actualizado parcialmente el nuevo dato {update_partial_post.status_code}"

#     except:
#         return "No se ha podido crear, ha ocurrido un problema"

# name = str(input("Dame un nombre: "))

# result = create_new_post(name)

# print(result)




# # * 5


# def create_new_post(data):
#     try:

#         update_post = requests.delete("https://jsonplaceholder.typicode.com/posts/1", json = data)
#         if(int(update_post.status_code) == 200):
#             return f"Se ha borrado correctamente el nuevo dato {update_post.status_code}"

#     except:
#         return "No se ha podido crear, ha ocurrido un problema"


# id = int(input("Dime un ID entero a borrar: "))

# data = {"id" : id}

# result = create_new_post(data)

# print(result)








