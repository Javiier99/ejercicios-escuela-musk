







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
















# # ! Ejercicio 2

# import json
# def open_file_read():
#     with open("segunda_parte_apis/ejercicio-123/ej2.json", "r", encoding="utf-8") as file:
#         file_read = json.load(file)
#     return file_read

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



# # * 7

# def test_more_3_hours():
#     save_dates = []
#     read_file = open_file_read()
#     for i in read_file:
#         if(i['Horas'] > 3):
#             save_dates.append(i['Titulo'])
#     return save_dates

# result = test_more_3_hours()
# print(f"Los titulos que cumple son: {result}")



# # * 8


# def where_there_is_test():
#     read_file = open_file_read()
#     count_in_person = 0
#     count_remote = 0
#     for i in read_file:
#         word_remote_or_in_person = i['TipoFormacion'].replace(" ","").lower()
#         if(word_remote_or_in_person == "nopresencial"):
#             count_remote += 1
#         elif(word_remote_or_in_person == "presencial"):
#             count_in_person += 1
#     type_trainig = {"No Presencial": count_remote, "Presencial" : count_in_person}
#     return type_trainig

# result = where_there_is_test()
# print(result)


# # * 9

# def shortest_test():
#     read_file = open_file_read()
#     save_hour_short = 10
#     save_hour_long = 0
#     save_data_short = []
#     save_data_long = []

#     for i in read_file:
#         if(int(i['Horas']) > save_hour_long):
#             save_data_long = [i['Titulo'], int(i['Horas'])]
#             save_hour_long = i['Horas']
#         if(int(i['Horas']) < save_hour_short):
#             save_data_short = [i['Titulo'], int(i['Horas'])]
#             save_hour_short = i['Horas']

#     result = [save_data_long, save_data_short]
#     return result

# result = shortest_test()
# print(result)



# # * 10

# from datetime import datetime

# def date_search(date_user):
#     read_file = open_file_read()
#     coincidences = []
#     for i in read_file:

#         start_date = i['InicioImparticion']
#         start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
#         date_formatting_start = start_date.strftime("%d-%m-%Y")


#         end_date = i['FinImparticion']
#         end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S")
#         date_formatting_end = end_date.strftime("%d-%m-%Y")

#         date_user_1 = datetime.strptime(date_user, "%d-%m-%Y")
#         date_user_formating_end = date_user_1.strftime("%d-%m-%Y")

#         if((date_formatting_start == date_user_formating_end) or (date_formatting_end == date_user_formating_end)):
#             coincidences.append(i['Titulo'])
#     return coincidences

# date_user = str("12-01-2015")
# result = date_search(date_user)
# print(result)




# # * 11

# def search_name_teachers(name):

#     result = []
#     read_file = open_file_read()
#     for i in read_file:
#         teachers = i['Profesorado']
#         for x in teachers:
#             name_teachers = x['NombreCompleto'].strip().lower()
#             if(name in name_teachers):
#                 result.append(i['Nivel'])

#     return result


# name = str(input("Di un nombre: "))
# name_modified = name.strip().lower()

# read_file = open_file_read()
# result = search_name_teachers(name_modified)
# print(f"La prueba que tiene el nombre: {name} es: {result}")





# # * 12


# def search_test_all_data(title_search):
#     read_file = open_file_read()
#     count = 0
#     for i in read_file:
#         if(title_search in i['Titulo']):
#             return read_file[count]
#         count += 1
#     return "No se encuentra o está mal escrito"



# # title_search = str(input("Escribe el nombre del titulo: "))
# title_search = "Inglés - Prueba de nivel - Para preparatorios del FCE/CAE/CPE/IELTS"
# all_data = search_test_all_data(title_search)
# print(all_data)











# ! Ejercicio 3


import json
import ijson

def file_open_read():
    with open("segunda_parte_apis/ejercicio-123/ej3.json", "rb") as file:
        for i in ijson.items(file, "lista.provincia.item"):
            yield i

open_read_line = file_open_read()

def borrar():
    for i in open_read_line:
        name_province = i['nombre']['__cdata']

        town = i.get("localidades", {}).get("localidad", [])

        if isinstance(town, list):
            for x in town:
                town_alone = x['__cdata']

        elif isinstance(town, dict):
            town_alone = town['__cdata']
    


# * 1

# def all_province():
#     for i in open_read_line:
#         name_province = i['nombre']['__cdata']
#         print(name_province)

# result = all_province()




# # * 2

# def all_municipalities():
#     for i in open_read_line:

#         town = i.get("localidades", {}).get("localidad", [])

#         if isinstance(town, list):
#             for x in town:
#                 town_alone = x['__cdata']
#                 print(town_alone)

#         elif isinstance(town, dict):
#             town_alone = town['__cdata']
#             print(town_alone)
        

# result = all_municipalities()

# # * 3

# def province_municipalities_count():
#     for i in open_read_line:
#         name_province = i['nombre']['__cdata']

#         town = i.get("localidades", {}).get("localidad", [])
#         count_town = 0
#         for y in town:
#             if isinstance(y, list):
#                 for x in town:
#                     town_alone = x['__cdata']
#                     count_town += 1

#             elif isinstance(y, dict):
#                 town_alone = y['__cdata']
#                 count_town += 1

#         print(f"La provincia: {name_province} tiene una cantidad de {count_town} pueblos o ciudades")


# province_municipalities_count()




# # * 4


# def search_province_and_its_municipalities(province):
#     find = False
#     save_province = {province: []}
#     for i in open_read_line:
#         name_province = str(i['nombre']['__cdata']).replace(" ","").upper()
#         if(name_province == province):
#             town = i.get("localidades", {}).get("localidad", [])
#             for y in town:
#                 if isinstance(y, list):
#                     for x in town:
#                         town_alone = x['__cdata']
#                         save_province[province].append(town_alone)

#                 elif isinstance(y, dict):
#                     town_alone = y['__cdata']
#                     save_province[province].append(town_alone)

#             find = True

#         if(find == True):
#             break
#     return save_province



# province = str(input("Dame el nombre de la provincia: ")).replace(" ","").upper()

# result = search_province_and_its_municipalities(province)

# print(result)



# * 5

def agree_town(town_alone, town_client):
    if(town_alone == town_client):
        agree = True
        return agree
    else:
        agree = False
        return agree

def search_province_and_its_municipalities(town_client):

    for i in open_read_line:
        name_province = str(i['nombre']['__cdata'])
        town = i.get("localidades", {}).get("localidad", [])
        result = False
        if isinstance(town, list):
            for x in town:
                town_alone = str(x['__cdata']).replace(" ", "").upper()
                town_alone_save = x['__cdata']
                result = agree_town(town_alone, town_client)

                if(result == True):
                    print(f"El pueblo de {town_client} está en la provincia de: {name_province}")

        elif isinstance(town, dict):
            town_alone = str(town['__cdata']).replace(" ", "").upper()
            town_alone_save = town['__cdata']
            result = agree_town(town_alone, town_client)

        if(result == True):
            print(f"El pueblo de {town_alone_save} está en la provincia de: {name_province}")
            return



# town_client = "Aljaraque".upper()
town_client = str(input("Dime el nombre de un pueblo: "))

search_province_and_its_municipalities(town_client)



# * 6



# en una lista tenemos distintos identificadores de provincias, devolver el nombre de las
# provincias y todos los municipios correspondientes a los identificadores que se encuentran
# en la lista.
