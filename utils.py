import numpy as np

# Função que adiciona um registro à base de dados
def add_person(data: dict, name: str, age: int, city: str, hobbies: list) -> dict:
    """Função que adiciona um registro à base de dados
    
    Parameters
    ----------
    data : dict
        Base de dados.
    name : str
        Nome da pessoa a ser registrada.
    age : int
        Idade da pessoa.
    city : str
        Cidade da pessoa.
    hobbies : list
        Hobbies da pessoa.

    Returns
    -------
    dict
        Base de dados com o registro adicionado.
    """

    new_person = {}
    new_person["name"] = name
    new_person["age"] = age
    new_person["city"] = city
    new_person["hobbies"] = hobbies

    if age < 0 or age > 100:
        try:
            raise ValueError
        except ValueError:
            print("A idade deve ser um inteiro entre 0 e 100.\n")
            return data
        
    if type(city) != str:
        try:
            raise TypeError
        except:
            print("O valor passado para a cidade não é uma string.\n")
            return data
        
    if len(hobbies) == 0:
        try:
            raise ValueError
        except:
            print("A lista de hobbies não pode ser vazia.\n")
            return data

    for person in data:
        if person["name"] == name:
            print("Já existe uma pessoa listada com esse nome.\n")
            return data

    data.append(new_person)

    return data

# Função que remove um registro da base de dados
def remove_person(data: dict, name: str) -> dict:
    """Função que remove um registro da base de dados
    
    Parameters
    ----------
    data : dict
        Base de dados.
    name : str
        Nome da pessoa a ser removida dos registros.

    Returns
    -------
    dict
        Base de dados com o registro removido.
    """
        
    for person in data:
        if person["name"] == name:
            data.remove(person)
            return data
        
    print("Não existe nenhuma pessoa listada com esse nome.\n")
    return data

# Função que entrega as idades mínima, média e máxima dos registros
def get_ages(data: dict) -> tuple:
    """Função que entrega as idades mínima, média e máxima dos registros
    
    Parameters
    ----------
    data : dict
        Base de dados.

    Returns
    -------
    tuple
        Tupla com a idade mínima, a idade média e a idade máxima dos registros.
    """

    ages = []
    for person in data:
        ages.append(person["age"])

    media = np.mean(ages)

    return (min(ages), int(media), max(ages))

# Função que entrega um conjunto com todos os hobbies dos registros
def get_hobbies(data: dict) -> set:
    """Função que entrega um conjunto com todos os hobbies dos registros
    
    Parameters
    ----------
    data : dict
        Base de dados.

    Returns
    -------
    set
        Conjunto com todos os hobbies dos registros.
    """

    hobbies = set()
    for person in data:
        for hobby in person["hobbies"]:
            hobbies.add(hobby)

    return hobbies

# Função que entrega registros que possuem os hobbies especificados
def get_people_by_hobbies(data: dict, hobbies: list) -> list:
    """Função que entrega registros que possuem os hobbies especificados
    
    Parameters
    ----------
    data : dict
        Base de dados.
    hobbies : list
        Lista de hobbies a serem procurados.

    Returns
    -------
    list
        Lista com os registros favoráveis.
    """

    people_with_ages = {}
    for person in data:
        for hobby in hobbies:
            if hobby in person["hobbies"] and person["name"] not in people_with_ages.keys():
                people_with_ages[person["name"]] = person["age"]

    people_with_ages_ordered = sorted(people_with_ages.items(), key = lambda x: x[1])
    people_ordered = [tupla[0] for tupla in people_with_ages_ordered]

    return people_ordered

# Função que entrega registros de acordo com os filtros utilizados
def match_people(data: dict, name: str = None, min_age: int = None, max_age: int = None, city: str = None, hobbies: list = []) -> list:
    """Função que entrega registros de acordo com os filtros utilizados
    
    Parameters
    ----------
    data : dict
        Base de dados.
    name : str
        Nome do registros.
    min_age : int
        Idade mínima dos registros.
    max_age : int
        Idade máxima dos registros.
    city : str
        Cidade dos registros.
    hobbies : list
        Hobbies dos registros.

    Returns
    -------
    list
        Lista com os registros favoráveis.
    """
    people_with_ages = {}
    for person in data:
        people_with_ages[person["name"]] = person["age"]

    people_with_ages_ordered = sorted(people_with_ages.items(), key = lambda x: x[1])
    people_ordered = [tuple[0] for tuple in people_with_ages_ordered]

    people_not_matched = set()

    if name != None:
        for person in data:
            if person["name"] != name:
                people_not_matched.add(person["name"])

    if min_age != None and max_age != None:
        if min_age > max_age:
            try:
                raise ValueError
            except:
                print("A idade mínima deve ser menor que a idade máxima.")
                return []
            
    if min_age != None:
        for person in data:
            if person["age"] < min_age:
                people_not_matched.add(person["name"])

    if max_age != None:
        for person in data:
            if person["age"] > max_age:
                people_not_matched.add(person["name"])

    if city != None:
        for person in data:
            if person["city"] != city:
                people_not_matched.add(person["name"])

    if len(hobbies) != 0:
        for person in data:
            for hobby in hobbies:
                if hobby not in person["hobbies"]:
                    people_not_matched.add(person["name"])
    
    for person in people_not_matched:
        people_ordered.remove(person)

    return people_ordered