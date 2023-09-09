import data
import utils

people_data = data.people_data

print(help(utils.match_people))

### Execução normal da 1° função
# print(utils.add_person(people_data, "Pedro", 18, "Rio de Janeiro", ["videogames", "movies"]), "\n")

### Execução da 1° função com idade negativa
# print(utils.add_person(people_data, "Pedro", -10, "Rio de Janeiro", ["videogames", "movies"]), "\n")

### Execução da 1° função com idade acima de 100
# print(utils.add_person(people_data, "Pedro", 120, "Rio de Janeiro", ["videogames", "movies"]), "\n")

### Execução da 1° função com a cidade não string
# print(utils.add_person(people_data, "Pedro", 18, 10, ["videogames", "movies"]), "\n")

### Execução da 1° função com a lista de hobbies vazia
# print(utils.add_person(people_data, "Pedro", 18, "Rio de Janeiro", []), "\n")

### Execução da 1° função com pessoa repetida
# print(utils.add_person(people_data, "Alice", 18, "Rio de Janeiro", ["videogames", "movies"]), "\n")



### Execução normal da 2° função
# print(utils.remove_person(people_data, "Alice"), "\n")

### Execução da 2° função com pessoa inexistente
# print(utils.remove_person(people_data, "Mark"), "\n")



### Execução da 3° função
# print(utils.get_ages(people_data))



### Execução da 4° função
# print(utils.get_hobbies(people_data))



### Execução da 5° função
# print(utils.get_people_by_hobbies(people_data, {"hiking", "gardening"}))

### Execução da 5° função com um conjunto vazio
# print(utils.get_people_by_hobbies(people_data, {}))



### Execução da 6° função sem nenhum argumento opcional
# print(utils.match_people(people_data))

### Execução da 6° função com um argumento opcional
# print(utils.match_people(people_data, min_age = 25))

### Execução da 6° função com erro nas idades
# print(utils.match_people(people_data, min_age = 25, max_age = 22))

### Execução da 6° função com alguns argumentos opcionais
# print(utils.match_people(people_data, min_age = 22, max_age = 26))

### Execução da 6° função com todos os argumentos opcionais
# print(utils.match_people(people_data, 
#                          name = "Alice", 
#                          min_age = 22, 
#                          max_age = 26, 
#                          city = "New York",
#                          hobbies = ["hiking", "reading"]))

### Execução da 6° função sem nenhuma correspondência
# print(utils.match_people(people_data, 
#                          name = "Alice", 
#                          min_age = 22, 
#                          max_age = 26, 
#                          city = "San Francisco",
#                          hobbies = ["hiking", "reading"]))