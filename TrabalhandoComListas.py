import this

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
