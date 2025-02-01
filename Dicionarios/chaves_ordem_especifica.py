# chaves_ordem_especifica.py

# Inicializa o dicionário com as linguagens favoritas.
linguagem_favorita = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
}

# Percorre as chaves do dicionário em ordem específica (alfabética).
for name in sorted(linguagem_favorita.keys()):
    print(f"{name.title()}")
