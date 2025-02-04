# descrever_pet_argumentos_nomeados.py

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print(f"\nEu tenho um {animal_type}.")
    print(f"O nome do meu {animal_type} é {pet_name.title()}.")

# Descreve um animal de estimação usando argumentos nomeados.
describe_pet(animal_type='hamster', pet_name='harry')
