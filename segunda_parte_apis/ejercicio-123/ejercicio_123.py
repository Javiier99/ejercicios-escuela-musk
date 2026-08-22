



import json



# ! Ejercicio 1

with open("segunda_parte_apis/ejercicio-123/ej1.json", encoding="utf-8") as file:
    file_load = json.load(file)


# # * 1

# count = 0
# for i in file_load['bookstore']['book']:
#     count += 1

# print(f"Tenemos {count} libros")



# # * 2

# limit_price_min = float(input("Señala un límite mínimo para el precio del libro "))
# limit_price_max = float(input("Señala un límite máximo para el precio del libro "))
# save_data = dict()

# for i in file_load['bookstore']['book']:
#     if (limit_price_min < float(i['price']) < limit_price_max ):
#         save_data = i
#         print(f"Un libro está cerca de tu resultado llamado: {save_data['title']['__text']} cuyo precio es {save_data['price']}€  ")






# # * 3

# word_search = str(input("Selecciona una palabra a buscar ")).lower()

# for i in file_load['bookstore']['book']:
#     list_book = str(i['title']['__text']).lower().split()

#     for x in range(len(list_book)):
#         if(str(list_book[x]) == word_search):
#             print(f"La palabra que has colocado, tiene esta posible coincidencia: Nombre: {i['title']['__text']} Año de publicación: {i['year']}")




# # * 4

# for i in file_load['bookstore']['book']:
#     print(f"Los autores del libro: {i['title']['__text']} y su autor/es: {i['author']}")



# # *5

# def know_category(category):
#     save_data = []
#     for i in file_load['bookstore']['book']:
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
#     print(f"Los libros que pertenecen a la categoría {category} es {result}")




# # * 6


# def author_book(name_book):
#     save_data = []
#     for i in file_load['bookstore']['book']:
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
#     for i in file_load['bookstore']['book']:
#         if(float(i['price']) > save_number_tall):
#             save_data = i['title']['__text']
#             save_number_tall = float(i['price'])

#     return [save_data, save_number_tall]

# book_price_tall = greater_value()
# print(f"El nombre del libro es {book_price_tall[0]} y su precio es: {book_price_tall[1]}€")



# * 8 ¿Cuáles libros fueron publicados en un año específico? Implementa una función que reciba un año y devuelva una lista de títulos de los libros que fueron publicados en ese año.













