# modificando_lista_em_funcao.py

def print_models(unprinted_designs, completed_models):
    """Simula a impressão de cada design e move-os para a lista de concluídos."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Imprimindo modelo: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Exibe todos os modelos que foram impressos."""
    print("\nOs seguintes modelos foram impressos:")
    for completed_model in completed_models:
        print(completed_model)

# Lista de designs a serem impressos.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# Lista de designs já impressos.
completed_models = []

# Simula a impressão dos designs e exibe os concluídos.
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
