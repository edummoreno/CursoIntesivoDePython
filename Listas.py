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
