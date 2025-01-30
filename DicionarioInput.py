#preenchendo um dicionario com entrada do usuario

responses = {}

#define uma flag sinalizar que a pesquisa está ativa
polling_active = True

while polling_active:
    #solicita o nome e a resposta do participante
    name = input("\nWhat is your name? ")
    response = input("Which mountain would like to climb someday? ")

    #armazena a resposta no dicionário
    responses[name] = response

    #detecta se mais alguém participará da pesquisa
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#A pequisa está completa. Mostra os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



