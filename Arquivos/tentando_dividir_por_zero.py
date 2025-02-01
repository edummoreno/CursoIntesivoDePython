# Define os números para a operação de divisão.
numero_zero = 0
numero_um = 1

try:
    # Tenta realizar a divisão por zero, o que é matematicamente impossível.
    divisao_por_zero = numero_um / numero_zero
except ZeroDivisionError:
    # Informa ao usuário que a divisão por zero é impossível.
    print("Matematicamente não é possível dividir por zero.")
    divisao_por_zero = None  # Define a variável como None após capturar o erro.

# Tenta imprimir o resultado da divisão.
try:
    if divisao_por_zero is not None:
        print(f"O resultado da divisão é: {divisao_por_zero}")
    else:
        print("A variável 'divisao_por_zero' não contém um valor, pois a divisão por zero não foi realizada.")
except NameError:
    # Esta exceção não deve ocorrer neste caso, pois estamos usando 'divisao_por_zero' como uma variável definida.
    print("A variável não foi definida devido a uma operação anterior que falhou.")
