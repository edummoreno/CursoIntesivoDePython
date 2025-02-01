responses = {}

# Define uma flag para sinalizar que a pesquisa está ativa.
polling_active = True

while polling_active:
    # Solicita o nome e a resposta do participante.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Armazena a resposta no dicionário.
    responses[name] = response

    # Detecta se mais alguém participará da pesquisa.
    repeat = input("Would you like to let another person respond? (yes/no) ").lower()
    if repeat == 'no':
        polling_active = False

# A pesquisa está completa. Mostra os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
