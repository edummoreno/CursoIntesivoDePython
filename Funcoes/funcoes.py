def greet_user():
    """Exibe um cumprimento"""
    print("Olá, tudo bem?")


greet_user()

#passando informação para uma função

def greet_user1(username):
    """Exibe um cumprimento"""

    print(f"Ola {username}")


greet_user1('Eduardo')

#Argumentos e parametros

livro = input("Qual seu livro e bom?")

def livro_bom(livro):
    print(f"então o livro {livro} e bom?")

livro_bom(livro)

#argumentos possicionais
def describe_pet(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

#argumentos nomeados
def describe_pet1(animal_type, pet_name):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet1(animal_type='hamster',pet_name='harry')


#chamas de função equivalentes

def describe_pet(dog):
    print(dog)

"""um cachorro chamado Willie"""
describe_pet('Willie')
describe_pet(dog='Willie')


#evitando erros de argumento

#valores de retorno #retornando um valor simples

def get_formatted_name(first_name,last_name):
    """Retorna um nome completo, elegantemente formatado"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

#Defininado um argumento como opcional
def get_formatted_name(first_name, last_name, middle_name=''):
    """retorna um nome completo, formatado elegantemente"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john ', 'hooker', 'lee')
print(musician)

#retornando um dicionário

def build_person(first_name, last_name):
    """retorna um diccionario de informações sobre uma pessoa"""
    person = {'first': first_name, 'last':last_name}
    return person

musician = get_formatted_name('jimi','hendrix')
print(musician)


#usando uma função com um loop while
def get_formatted(first_name, last_name):
    """retorna um nome completo, formatado elegantemente"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name: ")
    if f_name == 'q':
        break

    l_name = input("Last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted(f_name,l_name)
    print(f"\nHello, {formatted_name}")
    break

#passando uma lista

def greet_user2(names):
    """exibe um simples hello para caca usuario na lista"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


username = ['quincy','robinson']


greet_user2(username)


#modificando uma lista em uma função

"""começa com alguns desings que precisam ser impressos"""
unprinted_designs = ['phone casa','robot pendant', 'dodecahedron']
completed_models = []

"""simula a impressão de cada desing, até que não reste nenhum"""
"""passsa cada design para completed_moedls apos impressão"""

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

"""Exibe todos os modelos concluidos"""
print("\nThe following have been printed:")
for completed_model in completed_models:
    print(completed_model)

#evitando que uma função modifique uma lista

