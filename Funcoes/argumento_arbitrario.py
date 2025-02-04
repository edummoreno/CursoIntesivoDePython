#passando um numero arbitrario de argumentos

def make_pizza(*toppings): 
    """Exibe a lista de ingrediente solicitados"""
    """o asteristco no nome do parâmetro informa ao python para criar uma tupla"""
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')