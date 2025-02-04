# criar_dicionario_pessoa.py

def get_formatted_name(first_name, last_name):
    """Retorna um nome completo, formatado de maneira elegante."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def build_person(first_name, last_name):
    """Retorna um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    return person

# Cria um dicionário para uma pessoa e depois usa a função get_formatted_name para imprimir o nome formatado.
musician_dict = build_person('jimi', 'hendrix')
musician_name = get_formatted_name(musician_dict['first'], musician_dict['last'])
print(musician_name)
