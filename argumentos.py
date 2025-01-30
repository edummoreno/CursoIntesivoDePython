#passando um numero arbitrario de argumentos

def make_pizza(*toppings): 
    """Exibe a lista de ingrediente solicitados"""
    """o asteristco no nome do parâmetro informa ao python para criar uma tupla"""
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#Misturando argumentos posicionais e arbitrários

def make_pizza1(size, *toppings):
    """Sintetiza a pissa ue estamos pestes a fazer"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms','green peppers')


#usando argumentos nomeados arbitratios