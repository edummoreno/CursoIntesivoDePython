# ===========================
#  Trabalhando com Instruções if
# ===========================

# Lista de carros
cars = ['audi', 'bmw', 'subaru', 'toyota']

# ===========================
#  Igualdade
# ===========================

for car in cars:
    if car == 'bmw':
        print(car.upper())  # Em maiúsculas se for 'bmw'
    else:
        print(car.title())  # Primeira letra maiúscula para os demais

# ===========================
#  Diferença
# ===========================

for car in cars:
    if car != 'bmw':
        print(car.upper())  # Em maiúsculas se não for 'bmw'
    else:
        print(car.title())  # Primeira letra maiúscula para 'bmw'

# ===========================
#  Múltiplas Condições
# ===========================

# Condição AND
age_0 = 21
age_1 = 21

if (age_0 >= 21) and (age_1 >= 21):
    print("Já pode dirigir, e beber com moderação")

# Condição OR
age_0 = 15
acompanhado = True

if (age_0 >= 16) or acompanhado:
    print("Pode ir no brinquedo!")

# ===========================
#  Verificando se Valor Está na Lista
# ===========================

users = ['andrew', 'caroline', 'david']  # Lista de usuários
user = 'eduardo'

if user not in users:
    print(f"{user.title()} não está na lista.")

# ===========================
#  Expressões Booleanas
# ===========================

game_active = True
can_edit = False

# ===========================
#  if e else
# ===========================

age = 27

# Verificando maioridade
if age >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")

# Várias condições com elif
if age < 4:
    print("Você é muito novo")
elif age < 65:
    print("Ainda não está velho")
else:
    print("Está na terceira idade")

# ===========================
#  if com Listas
# ===========================

# Verificando sabores de pizza
sabor_pizza = ['peperoni', 'extra cheese', 'portuguesa']

if 'peperoni' in sabor_pizza:
    print("Gostoso")
if 'extra cheese' in sabor_pizza:
    print("Delícia")
if 'portuguesa' in sabor_pizza:
    print("Ótimo")

# Exibindo os sabores disponíveis
for sabor in sabor_pizza:
    print(f"{sabor}")


#lista de dicionarios

alien_0 = {'color': 'green', 'points':5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

print(aliens)

print(f"total number of aliens: {len(aliens)}")

#uma lista em um dicionario
