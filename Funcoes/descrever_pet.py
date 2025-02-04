# descrever_pet.py

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print(f"\nEu tenho um {animal_type}.")
    print(f"O nome do meu {animal_type} é {pet_name.title()}.")

# Descreve um animal de estimação com informações passadas como argumentos.
describe_pet('hamster', 'harry')
