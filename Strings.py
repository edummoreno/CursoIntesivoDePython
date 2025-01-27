import string
import this

# ===========================
#  Manipulação de Strings
# ===========================

mensagem = "Hello World!!! faz o que da! melhor feito do que bem feito! - lembre-se crtl shit p"

print(mensagem.title())  # Primeira letra de cada palavra em maiúscula
print(mensagem.upper())  # Tudo em maiúsculas
print(mensagem.lower())  # Tudo em minúsculas

# ===========================
#  Concatenação de Strings
# ===========================

Primeiro_nome = "Eduardo"
Segundo_nome = "Moreno Neto"
nome_completo = f"{Primeiro_nome} {Segundo_nome}"

print("\t" + nome_completo)  # Exibindo nome com tabulação

# ===========================
#  Removendo Espaços em Branco
# ===========================

espaco = "    python    "

print(espaco.strip())   # Remove espaços dos dois lados
print(espaco.rstrip())  # Remove espaços à direita
print(espaco.lstrip())  # Remove espaços à esquerda

# ===========================
#  Removendo Prefixo e Sufixo
# ===========================

site = "https://google.com.br"

site = site.removeprefix('https://')  # Remove o prefixo "https://"
print(site)

site = site.removesuffix('.br')  # Remove o sufixo ".br"
print(site)

# ===========================
#  Trabalhando com Números
# ===========================

# Operações com inteiros
numero = 2 * 3
print(numero)

# Operações com números flutuantes
numero_float = 0.5 * 6
print(numero_float)

# Uso de underscore para melhorar a legibilidade de números grandes
underscore = 14_000_000_000
print(underscore)

# ===========================
#  Atribuição Múltipla
# ===========================

a, b, c = "a", "b", "c"
print(a + b + c)

