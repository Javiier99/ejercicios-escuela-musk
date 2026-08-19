



# # ? Ejercicio 1


# class Jet:
#     def __init__(self,name, country):
#         self.name = name
#         self.origin = country

# first_item = Jet("F16", "USA")

# print(f"El avión es un {first_item.name} del pais {first_item.origin}")



# # ? Ejercicio 2


# class Jet:
#     def __init__(self,name, country):
#         self.name = name
#         self.origin = country

# item_1 = Jet("F16", "USA")
# item_2 = Jet("SU33","Russia")
# item_3 = Jet("AJS37","Sweden")
# item_4 = Jet("Mirage2000","France")
# item_5 = Jet("F14","USA")
# item_6 = Jet("Mig29","USSR")
# item_7 = Jet("A10","USA")


# # ? Ejercicio 3
# class Jet:
#     def __init__(self,name, country, amount):
#         self.name = name
#         self.origin = country
#         self.amount = amount


# item_4 = Jet("Mirage2000","France", 87)
# item_5 = Jet("F14","USA", 35)




# # ? Ejercicio 4


# class Nobel:
#     def __init__(self, prize_category, year, name):
#         self.category = prize_category
#         self.year = year
#         self.winner = name

# np2005 = Nobel("Peace", 2005, "Mujammad Yunus")

# print(np2005.category, np2005.year, np2005.winner)


# # ? Ejercicio 5

# class Estudiante:
#     def __init__(self, nombre, edad, grado):
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado

# estudiante_1 = Estudiante("Javier", 27, "Python")

# print(estudiante_1.nombre, estudiante_1.edad, estudiante_1.grado)







# # ? Ejercicio 6

# class Estudiante:
#     pass




# # ? Ejercicio 7
# class Estudiante:
#     def __init__(self, name, math, language, history, philosophy):
#         self.name = name
#         self.math = math
#         self.language = language
#         self.history = history
#         self.philosophy = philosophy
#         self.grade = 0
    
#     def results(self):
#         list_subjects = [self.math, self.language, self.history, self.philosophy]
#         self.grade = sum(list_subjects) / len(list_subjects)
#         return self.grade


# studend_1 = Estudiante("Javier", 7, 3, 10, 8)
# studend_2 = Estudiante("Pablo", 2, 8, 1, 9)

# print(studend_1.results())
# print(studend_2.results())







# # ? Ejercicio 8

# class Estudiante:
#     def __init__(self, name, math, language, history, philosophy):
#         self.name = name
#         self.math = math
#         self.language = language
#         self.history = history
#         self.philosophy = philosophy
#         self.grade = 0
    
#     def results(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         self.grade = sum(list_subjects_result) / len(list_subjects_result)
#         return self.grade
    
#     def subjects_below_5(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         list_subjects = ["math", "language", "history", "philosophy"]
#         list_below_5 = []
#         for i in range(len(list_subjects)):
#             if(list_subjects_result[i] < 5):
#                 list_below_5.append(list_subjects[i])
#         return list_below_5


# studend_1 = Estudiante("Javier", 7, 3, 10, 8)
# studend_2 = Estudiante("Pablo", 2, 8, 1, 9)

# print(studend_1.subjects_below_5())
# print(studend_2.subjects_below_5())





# # ? Ejercicio 9

# class Estudiante:
#     school = "primaria"
#     def __init__(self, name, math, language, history, philosophy):
#         self.name = name
#         self.math = math
#         self.language = language
#         self.history = history
#         self.philosophy = philosophy
#         self.grade = 0
    
#     def results(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         self.grade = sum(list_subjects_result) / len(list_subjects_result)
#         return self.grade
    
#     def subjects_below_5(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         list_subjects = ["math", "language", "history", "philosophy"]
#         list_below_5 = []
#         for i in range(len(list_subjects)):
#             if(list_subjects_result[i] < 5):
#                 list_below_5.append(list_subjects[i])
#         return list_below_5
#     @classmethod
#     def cambiar_escuela(cls, new_school):
#         cls.school = new_school
#         return new_school


# studend_1 = Estudiante("Javier", 7, 3, 10, 8)
# studend_2 = Estudiante("Pablo", 2, 8, 1, 9)

# print(f"El Estudiante {studend_1.name} va a la escuela {studend_1.school}")

# studend_1.cambiar_escuela("Secundaria")

# print(f"El Estudiante {studend_2.name} va a la escuela {studend_2.school}")




# # ? Ejercicio 10



# class Estudiante:
#     school = "primaria"
#     def __init__(self, name, math, language, history, philosophy):
#         self.name = name
#         self.math = math
#         self.language = language
#         self.history = history
#         self.philosophy = philosophy
#         self.grade = 0
#         self.assistnace = 0
    
#     def results(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         self.grade = sum(list_subjects_result) / len(list_subjects_result)
#         return self.grade
    
#     def subjects_below_5(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         list_subjects = ["math", "language", "history", "philosophy"]
#         list_below_5 = []
#         for i in range(len(list_subjects)):
#             if(list_subjects_result[i] < 5):
#                 list_below_5.append(list_subjects[i])
#         return list_below_5
#     @classmethod
#     def cambiar_escuela(cls, new_school):
#         cls.school = new_school
#         return new_school
    
#     def assistnace_student(self):
#         self.assistnace = int(input(f"Nº de asistencias que ha tenido el alumno {self.name} (Escoge entre el 1 - 8): "))
#         result_attendance = self.__assistance_priv()
#         print(f"El alumno {studend_1.name} ha tenido una asistencia de {self.assistnace} del cual le dará un resultado de {result_attendance} puntos") 
    
#     def __assistance_priv(self):
#         if(self.assistnace == 1):
#             return 1
#         elif(self.assistnace < 4):
#             return 2
#         elif((self.assistnace >= 4) and (self.assistnace <= 8)):
#             return 3
        


# studend_1 = Estudiante("Javier", 7, 3, 10, 8)
# studend_2 = Estudiante("Pablo", 2, 8, 1, 9)

# studend_1.assistnace_student()






# # ? Ejercicio 11 Mejora 



# class Estudiante:
#     school = "primaria"
#     def __init__(self, name, math, language, history, philosophy):
#         self.name = name
#         self.math = math
#         self.language = language
#         self.history = history
#         self.philosophy = philosophy
#         self.grade = 0
#         self.assistnace = 0
    
#     def results(self):
#         list_subjects_result = [self.math, self.language, self.history, self.philosophy]
#         self.grade = sum(list_subjects_result) / len(list_subjects_result)
#         return self.grade
    
#     def failed_subject(self):
#         dictionary = {
#                 "Name": self.name, 
#                 "Subjects" : {
#                         "Math" : self.math, 
#                         "Language" : self.language, 
#                         "History" : self.history, 
#                         "Philosophy" : self.philosophy
#                 }
#         }
#         list_below_5 = []
#         list_subjects_5 = []
#         lists_together = ""
#         point_subjects = 0
#         # * Necesito saber que materias están suspensas
#         for i in range(len(dictionary["Subjects"].values())):
#             if(list(dictionary["Subjects"].values())[i] < 5):
#                 list_below_5.append(list(dictionary["Subjects"].values())[i])
#                 list_subjects_5.append(list(dictionary["Subjects"].keys())[i])
        
#         # * Para hacerlo más profesional tengo que juntar las dos listas
#         for i in range(len(list_below_5)):
#             lists_together += (f"{list_subjects_5[i]} : {list_below_5[i]}, ")
#             point_subjects += 1
        
#         if(point_subjects == 0):
#             result = f"El alumno {self.name} no ha suspendido ningúna asignatura"
#         elif(point_subjects == 1):
#             result = f"El alumno {self.name} ha suspendido esta materia: {lists_together} por lo que debe de repetir"
#         elif(point_subjects > 1):
#             result = f"El alumno {self.name} ha suspendido estas materias: {lists_together} por lo que debe de repetir"
#         return result

#     @classmethod
#     def cambiar_escuela(cls, new_school):
#         cls.school = new_school
#         return new_school
    
#     def assistnace_student(self):
#         self.assistnace = int(input(f"Nº de asistencias que ha tenido el alumno {self.name} (Escoge entre el 1 - 8): "))
#         result_attendance = self.__assistance_priv()
#         print(f"El alumno {studend_1.name} ha tenido una asistencia de {self.assistnace} del cual le dará un resultado de {result_attendance} puntos") 
    
#     def __assistance_priv(self):
#         if(self.assistnace == 1):
#             return 1
#         elif(self.assistnace < 4):
#             return 2
#         elif((self.assistnace >= 4) and (self.assistnace <= 8)):
#             return 3
        


# studend_1 = Estudiante("Javier", 7, 3, 10, 1)
# studend_2 = Estudiante("Pablo", 2, 8, 1, 9)


# print(studend_1.failed_subject())






# ? Ejercicio 12 Mejora

class Estudiante:
    school = "primaria"
    def __init__(self, name, subjects_and_result):
        self.name = name
        self.subjects_and_result = subjects_and_result
        self.grade = 0
        self.assistnace = 0
    
    def results(self):
        list_subjects_result = [self.math, self.language, self.history, self.philosophy]
        self.grade = sum(list_subjects_result) / len(list_subjects_result)
        return self.grade
    
    def failed_subject(self):
        list_below_5 = []
        list_subjects_5 = []
        lists_together = ""
        point_subjects = 0
        # * Necesito saber que materias están suspensas
        for i in range(len(self.subjects_and_result.values())):
            if(list(self.subjects_and_result.values())[i] < 5):
                list_below_5.append(list(self.subjects_and_result.values())[i])
                list_subjects_5.append(list(self.subjects_and_result.keys())[i])
        
        # * Para hacerlo más profesional tengo que juntar las dos listas
        for i in range(len(list_below_5)):
            lists_together += (f"{list_subjects_5[i]} : {list_below_5[i]}, ")
            point_subjects += 1
        
        if(point_subjects == 0):
            result = f"El alumno {self.name} no ha suspendido ningúna asignatura"
        elif(point_subjects == 1):
            result = f"El alumno {self.name} ha suspendido esta materia: {lists_together} por lo que debe de repetir"
        elif(point_subjects > 1):
            result = f"El alumno {self.name} ha suspendido estas materias: {lists_together} por lo que debe de repetir"
        return result

    @classmethod
    def cambiar_escuela(cls, new_school):
        cls.school = new_school
        return new_school
    
    def assistnace_student(self):
        self.assistnace = int(input(f"Nº de asistencias que ha tenido el alumno {self.name} (Escoge entre el 1 - 8): "))
        result_attendance = self.__assistance_priv()
        print(f"El alumno {studend_1.name} ha tenido una asistencia de {self.assistnace} del cual le dará un resultado de {result_attendance} puntos") 
    
    def __assistance_priv(self):
        if(self.assistnace == 1):
            return 1
        elif(self.assistnace < 4):
            return 2
        elif((self.assistnace >= 4) and (self.assistnace <= 8)):
            return 3
        

subjects_and_result_studend_1 = {"Math" : 6, "Language" : 5, "History" : 5, "Philosophy" : 6, "Geography" : 3}
studend_1 = Estudiante("Javier", subjects_and_result_studend_1)
subjects_and_result_studend_2 = {"Math" : 10, "Language" : 1, "History" : 7, "Geography" : 3}
studend_2 = Estudiante("Pablo", subjects_and_result_studend_2)


print(studend_1.failed_subject())
print(studend_2.failed_subject())

