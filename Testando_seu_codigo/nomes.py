from get_formatted_name import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
    first = input("Digite seu primeiro nome: ")
    if first == 'q':
        break
    last = input("Digite seu sobrenome: ")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f"Seu nome e {formatted_name}")    