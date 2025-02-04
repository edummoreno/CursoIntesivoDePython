# nome_completo_opcional.py

def get_formatted_name(first_name, last_name, middle_name=''):
    """Retorna um nome completo, com opção de incluir um nome do meio."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Exemplos de uso da função com e sem nome do meio.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
