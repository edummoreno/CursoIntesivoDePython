# usando_get.py

# Inicializa o dicionário com os valores iniciais.
alien_0 = {'color': 'green', 'speed': 'slow'}

# Usa o método get() para acessar o valor associado à chave 'points'.
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
