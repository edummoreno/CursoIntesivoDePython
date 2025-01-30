# ===========================
#  Entrada de Dados com input()
# ===========================

# Solicitando o nome do usuário
name = input("Please enter your name: ")
print(f"Olá, {name}!")

# ===========================
#  Entrada de Números Inteiros
# ===========================

idade = int(input("Qual sua idade? "))
print(f"Idade: {idade}")

# ===========================
#  Operador Módulo (%)
# ===========================

# Verificando se um número é par ou ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
