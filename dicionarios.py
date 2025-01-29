# ===========================
#  Dicionário Simples
# ===========================

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(f"Você fez {alien_0['points']} pontos")

# ===========================
#  Adicionando Novos Pares Chave-Valor
# ===========================

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# ===========================
#  Criando um Dicionário Vazio e Adicionando Valores
# ===========================

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# ===========================
#  Modificando Valores no Dicionário
# ===========================

print(f"Cor do alien é {alien_0['color']}")

alien_0['color'] = 'blue'
print(f"Agora a nova cor é {alien_0['color']}")

# ===========================
#  Removendo um Par Chave-Valor
# ===========================

del alien_0['points']
print(alien_0)

# ===========================
#  Dicionário de Objetos Similares
# ===========================

linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
}

print(linguagem_favorita)

# ===========================
#  Usando get() para Acessar Valores
# ===========================

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# ===========================
#  Percorrendo um Dicionário com um Loop
# ===========================

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# O método .items() retorna pares chave-valor de um dicionário.
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# ===========================
#  Percorrendo Todas as Chaves de um Dicionário
# ===========================

for name in linguagem_favorita.keys():  # .keys() retorna somente as chaves do dicionário
    print(name.title())

# ===========================
#  Percorrendo as Chaves em Ordem Específica
# ===========================

for name in sorted(linguagem_favorita.keys()):
    print(f"{name.title()}")

# ===========================
#  Percorrendo Todos os Valores de um Dicionário
# ===========================

for language in linguagem_favorita.values():
    print(language.title())

# ===========================
#  Lista de Dicionários
# ===========================

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# ===========================
#  Lista Dentro de um Dicionário
# ===========================

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

for topping in pizza['toppings']:
    print(f"\t{topping}")

# ===========================
#  Dicionário Dentro de um Dicionário
# ===========================

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie'
    },
}

print(users)
