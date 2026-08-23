







# # ! Ejercicio 1

# import json

# with open("segunda_parte_apis/ejercicio-123/ej1.json", "r", encoding="utf-8") as file:
#     file_load = json.load(file)
#     object_file = file_load['bookstore']['book']


# # * 1

# count = 0
# for i in object_file:
#     count += 1

# print(f"Tenemos {count} libros")



# # * 2

# limit_price_min = float(input("Señala un límite mínimo para el precio del libro "))
# limit_price_max = float(input("Señala un límite máximo para el precio del libro "))
# save_data = dict()

# for i in object_file:
#     if (limit_price_min < float(i['price']) < limit_price_max ):
#         save_data = i
#         print(f"Un libro está cerca de tu resultado llamado: {save_data['title']['__text']} cuyo precio es {save_data['price']}€  ")






# # * 3

# word_search = str(input("Selecciona una palabra a buscar ")).lower()

# for i in object_file:
#     list_book = str(i['title']['__text']).lower().split()

#     for x in range(len(list_book)):
#         if(str(list_book[x]) == word_search):
#             print(f"La palabra que has colocado, tiene esta posible coincidencia: Nombre: {i['title']['__text']} Año de publicación: {i['year']}")




# # * 4

# for i in object_file:
#     print(f"Los autores del libro: {i['title']['__text']} y su autor/es: {i['author']}")



# # *5

# def know_category(category):
#     save_data = []
#     for i in object_file:
#         if(str(i['_category']) == category):
#             save_data.append(i['title']['__text'])

#     return save_data

# category = str(input("Escribe una categoría ")).upper()

# result = know_category(category) # Debe de recibir una categoría
# if(len(result) >= 2):
#     result = ", ".join(result)
#     print(f"Los libros que pertenecen a la categoría {category} son {result}")
# else:
#     result = "".join(result)
#     print(f"El libro que pertenece a la categoría {category} es {result}")




# # * 6


# def author_book(name_book):
#     save_data = []
#     for i in object_file:
#         if(str(i['title']['__text']).upper() == name_book):
#             author = i['author']
#             if isinstance(author, list):
#                 save_data.extend(author)
#             else:
#                 save_data.append(i['author'])
#     return save_data


# name_book = str(input("Dime un nombre de un líbro ")).upper()
# result = author_book(name_book)
# if(len(result) >= 2):
#     result = ", ".join(result)
#     print(f"El nombre del libro: {name_book} tiene estos autores {result}")
# else:
#     result = "".join(result)
#     print(f"El nombre del libro: {name_book} tiene este autor {result}")




# # * 7


# def greater_value():
#     save_data = ""
#     save_number_tall = 0
#     for i in object_file:
#         if(float(i['price']) > save_number_tall):
#             save_data = i['title']['__text']
#             save_number_tall = float(i['price'])

#     return [save_data, save_number_tall]

# book_price_tall = greater_value()
# print(f"El nombre del libro es {book_price_tall[0]} y su precio es: {book_price_tall[1]}€")



# # * 8 

# def years_public_book(year_book):
#     save_book = []
#     for i in object_file:
#         if(int(i['year']) == year_book):
#             save_book.append(i['title']['__text'])
#     return save_book


# year_book = int(input("Dime una fecha"))
# result = years_public_book(year_book)
# if(len(result) >= 2):
#     result = ", ".join(result)
#     print(f"El año del libro escogido: {year_book} tiene estos libros {result}")
# else:
#     result = "".join(result)
#     print(f"El año del libro escogido: {year_book} tiene este libro {result}")




# # * 9 

# def book_more_one_author():
#     save_book_author = []
#     for i in object_file:
#         author =  i['author']
#         if not isinstance(author, list):
#             author = [author]
#         if(len(author) >= 2):
#             book_name = i['title']['__text']
#             save_book_author.append(book_name)
#     return save_book_author


# result = book_more_one_author()
# result = ", ".join(result)
# print(f"Los libros con más de un autor son: {result}")




# # * 10


# def update_price_book(name_book, price_update):
#     save_book = ""
#     book_found = False
#     for i in object_file:
#         book = i['title']['__text']
#         if(book.lower() ==  name_book):
#             book_found = True
#             i['price'] = price_update

#     update = False
#     if(book_found == True):
#         with open("segunda_parte_apis/ejercicio-123/ej1.json", "w", encoding="utf-8") as file:
#             json.dump(file_load, file, indent= 4)
#         update = True

#     if(update == True):
#         return "Se ha actualizado con exito"
#     else:
#         return "No se ha actualizado porque no se ha encontrado el nombre"


# name_book = str(input("Cual es el libro que quieres actualizar el precio ").lower())
# # name_book = "harry potter"
# price_update = str(input("Que precio quieres actualizar "))
# # price_update = str(100)
# result = update_price_book(name_book, price_update)

# print(result)




# # *11

# def delete_book(name_book):
#     eliminated = False
#     try:
#         for i in range(len(object_file)):
#             name_book_file = object_file[i]['title']['__text']
#             if(name_book_file.upper() == name_book):
#                 del object_file[i]
#                 eliminated = True
#     except:
#         pass
#     if(eliminated == True): 
#         with open("segunda_parte_apis/ejercicio-123/ej1_ejercice_11.json", "w", encoding="utf-8") as file:
#             json.dump(file_load, file, indent = 4)
#             print("Editado")
#     else:
#         print("No se ha encontrado el nombre")

# name_book = str(input("Qué libro quieres eliminar? ")).upper()

# result = delete_book(name_book)


# # * 12

# # Menor a mayor
# def sort_book_date_year():
#     sort_book = []

#     for i in object_file:
#         title = i["title"]["__text"]
#         year = int(i["year"])
#         sort_book.append((title, year))

#     sort_book.sort(key = lambda x: x[1])
#     return sort_book

# result = sort_book_date_year()
# print(result)


# # * 13

# sum_price_all_book = 0
# book_less_than_price_average = []

# for i in object_file:
#     sum_price_all_book += float(i['price'])

# price_average = float(sum_price_all_book/int(len(object_file)))

# for i in object_file:
#     if(float(i['price']) < price_average):
#         book_less_than_price_average.append([i['title']['__text'],i['price']])

# print("Los libros por debajo del precio medio son: ", book_less_than_price_average)
















# ! Ejercicio 2

import json
def open_file_read():
    with open("segunda_parte_apis/ejercicio-123/ej2.json", "r", encoding="utf-8") as file:
        file_read = json.load(file)
    return file_read

# # * 1

# read_file = open_file_read()
# count = 0
# for i in read_file:
#     count += 1
# print(f"Tenemos {count} pruebas descritas en el documento")


# # * 2

# read_file = open_file_read()

# save_test = []
# for i in read_file:
#     if(int(i['Horas']) > 2):
#         save_test.append(i['Titulo'])

# print(f"Los titulos que duran más de 2 horas son: {save_test}")




# # * 3


# read_file = open_file_read()


# for i in read_file:
#     text_clean = i['TipoFormacion'].replace(" ","").lower()
#     if(text_clean == "nopresencial"):
#         print(f"La url es: {i['URL']}")


# # * 4

# save_datas = dict()
# read_file = open_file_read()

# for i in read_file:
#     if(i['$id'] not in save_datas):
#         save_datas[i['$id']] = []
#         save_datas[i['$id']].append(i['Titulo'])
    
#     for x in i['Profesorado']:
#         save_datas[i['$id']].append(x['NombreCompleto'])

# print(save_datas)



# # * 5


# save_datas = dict()
# read_file = open_file_read()

# for i in read_file:
#     if(i['Titulo'] not in save_datas):
#         save_datas[i['Titulo']] = []
    
#     for x in i['Profesorado']:
#         save_datas[i['Titulo']].append(x['NombreCompleto'])

# print(save_datas)



# # * 6

# save_dates = dict()
# read_file = open_file_read()

# for i in read_file:
#     if(i['$id'] not in save_dates):
#         save_dates[i['$id']] = [i['InicioImparticion'], i['FinImparticion']]

# print(save_dates)



# * 7

def test_more_3_hours():
    save_dates = []
    read_file = open_file_read()
    for i in read_file:
        if(i['Horas'] > 3):
            save_dates.append(i['Titulo'])
    return save_dates

result = test_more_3_hours()
print(f"Los titulos que cumple son: {result}")



# * 8
# ¿Cuántas pruebas de cada tipo de formación ("Presencial" y "No Presencial") hay?
# Implementa una función que devuelva un diccionario con el tipo de formación como clave y
# la cantidad de pruebas para cada tipo como valor















