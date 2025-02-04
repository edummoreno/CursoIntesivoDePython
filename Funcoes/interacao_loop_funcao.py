# interacao_loop_funcao.py

def get_formatted_name(first_name, last_name):
    """Retorna um nome completo, formatado de maneira elegante."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Loop que interage com o usuário para obter nomes e exibir cumprimentos.
while True:
    print("\nPor favor, me diga seu nome:")
    print("(digite 'q' a qualquer momento para sair)")

    f_name = input("Nome: ")
    if f_name == 'q':
        break

    l_name = input("Sobrenome: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nOlá, {formatted_name}")
    break  # Adicionado para garantir que o loop termine após a primeira iteração.
