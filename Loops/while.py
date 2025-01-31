#continuando input com While

#while

numero = 1
while numero < 10:
    print(numero)
    numero += 1

#permitindo que o usuario encerre o programa

prompt ="\nEnter para quit no programa: "

menssagem = ""


menssagem = input(prompt)



#usando flags
active = True

while active:
    menssagem = input('Escreva quit para sair do programa: ')

    if menssagem == 'quit':
        active = False
    else:
        print(menssagem)


#usando break para sair de um loop

prompt =  'Escreva quit para sair do programa: '

while True:
    menssagem = input(prompt)

    if menssagem == 'quit':
        break
    else:
        print(prompt)

#usando continue em um loop

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

#evitando loops infinitos

x = 1
while x <= 5:
    print(x)
    x +=1

#loop while com listas e dicionarios

lista = [1, 2, 3, 4, 5]
n = 0  # Comece do índice 0

while n < len(lista):  # Use "<" em vez de "<=" para evitar índice fora do intervalo
    print(lista[n])  # Use colchetes para acessar elementos da lista
    n += 1


#transferindo elementos de uma lista para outra

nao_confirmados = ['bruno','eduardo','kauane','castro']
confirmados = []

print(f"nao confirmados {nao_confirmados}")
print(f"confirmados {confirmados}")

while nao_confirmados:
    temporario = nao_confirmados.pop()

    confirmados.append(temporario)

    
print(f"nao confirmados {nao_confirmados}")
print(f"confirmados {confirmados}")

#removendo todas as instâncias de valores especificos de uma lista
pets = ['dog','cat','dog','goldfish','cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

