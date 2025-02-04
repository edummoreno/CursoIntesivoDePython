# cumprimento_lista_usuarios.py

def greet_user(names):
    """Exibe um cumprimento para cada usuário na lista."""
    for name in names:
        msg = f"Olá, {name.title()}!"
        print(msg)

# Lista de nomes de usuários.
username = ['quincy', 'robinson']

# Chama a função para cumprimentar cada usuário na lista.
greet_user(username)
