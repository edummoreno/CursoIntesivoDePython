import string

# ===========================
#  Trabalhando com Listas
# ===========================

# Definição de uma lista de bicicletas
bikes = ['caloi', 'eletrica', 'com marcha']

print(bikes)         # Exibe toda a lista
print(bikes[0])      # Exibe o primeiro item da lista
print(bikes[0].title())  # Exibe o primeiro item com a primeira letra maiúscula
print(bikes[-1])     # Exibe o último item da lista

# ===========================
#  Acessando Itens da Lista
# ===========================

nome = ['Eduardo', 'João', 'Jesus']

print("Bem vindo ", nome[0])
print("Bem vindo ", nome[1])
print("Bem vindo ", nome[2])

# ===========================
#  Modificando Listas
# ===========================

moto = ['yamaha', 'honda', 'nike']

# Modificando um item da lista
moto[2] = 'toyota'
print(moto[2])

# ===========================
#  Adicionando Elementos
# ===========================

# Adicionando um item ao final da lista
moto.append('ducati')
print(moto[3])

# Inserindo um item em uma posição específica
moto.insert(1, 'mistubishi')
print(moto[1])

# ===========================
#  Removendo Elementos
# ===========================

# Deletando um item da lista pelo índice
del moto[1]
print(moto)

# Removendo com pop() (remove o último item da lista e armazena em uma variável)
pop_moto = moto.pop()
print(moto)
print(pop_moto)

# Removendo item de uma posição específica
pop_moto = moto.pop(0)
print(pop_moto)

# Removendo elemento por valor (comentado para revisão)
# remove_moto = moto.remove('ducati')
# print(remove_moto)  # revisar

# ===========================
#  Ordenação de Listas
# ===========================

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)              # Lista original
print(sorted(cars))      # Lista ordenada temporariamente
cars.sort()              # Ordena permanentemente em ordem alfabética
print(cars)

cars.reverse()           # Inverte a ordem da lista
print(cars)

# ===========================
#  Trabalhando com Índices
# ===========================

# Importante: listas começam no índice 0
# Índice negativo [-1] exibe o último item da lista
print(len(cars))  # Exibe o tamanho da lista

# Observação:
# Listas em Python são definidas utilizando colchetes []


# ===========================
#  Trabalhando com Listas
# ===========================

magica = ['magico de oz', 'alice', 'harry potter']

# Loop for com listas
for magi in magica:
    print(magi)

# Observação: prestar atenção nos erros de identação e não esquecer os dois pontos ":"

# ===========================
#  Utilizando a Função range()
# ===========================

# Range de 1 a 5 (sempre usar um número a mais, ex: 6 para incluir até 5)
for value in range(1, 6):
    print(value)

# Criando lista com range()
num = list(range(1, 6))
print(num)

# ===========================
#  Números Pares e Ímpares com range()
# ===========================

par_num = list(range(2, 11, 2))  # De 2 a 10, pulando de 2 em 2 (pares)
print(par_num)

impar_num = list(range(1, 13, 2))  # De 1 a 12, pulando de 2 em 2 (ímpares)
print(impar_num)

# ===========================
#  Números ao Quadrado
# ===========================

quadrados = []
for value in range(1, 11):
    quadrado = value ** 2  # Eleva o valor ao quadrado
    quadrados.append(quadrado)

print(quadrados)

# ===========================
#  Estatísticas Simples com Listas Numéricas
# ===========================

lista_estatistica = []
for val in range(1, 11):
    lista_estatistica.append(val)

print(lista_estatistica)

# Mínimo, máximo e soma da lista
print(min(lista_estatistica))
print(max(lista_estatistica))
print(sum(lista_estatistica))

# ===========================
#  List Comprehensions (Listas Comprimidas)
# ===========================

# Gerando uma lista com apenas uma linha de código
quadrado = [val**2 for val in range(1, 11)]
print(quadrado)

# ===========================
#  Fatiamento de Listas
# ===========================

alfabeto = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']

print(alfabeto[0:3])  # Do início até índice 2 (não inclui o 3)
print(alfabeto[:4])   # Do início até índice 3
print(alfabeto[2:])   # Do índice 2 até o final

# Percorrendo uma fatia da lista com loop
for letra in alfabeto[:3]:
    print(letra.title())

# ===========================
#  Copiando uma Lista
# ===========================

copia_alfabeto = alfabeto[:]  # Copia completa da lista
print(copia_alfabeto)