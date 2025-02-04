#Misturando argumentos posicionais e arbitrários

def make_pizza1(size, *toppings):
    """Sintetiza a pissa ue estamos pestes a fazer"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms','green peppers')
