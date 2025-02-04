# nome_completo.py

def get_formatted_name(first_name, last_name):
    """Retorna um nome completo, formatado de maneira elegante."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Exemplo de uso da função com um nome completo.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
