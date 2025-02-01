from mpmath import mp

# Configura a precisão desejada para o cálculo de π.
mp.dps = 1000000

# Calcula π com a precisão configurada e converte para uma string.
pi_string = str(mp.pi)

# Remove o '3.' inicial para a busca, pois o aniversário não incluiria esses caracteres.
# Isso também torna a busca mais relevante para os dígitos decimais de π.
pi_decimals_only = pi_string[2:]

# Solicita ao usuário para digitar seu aniversário.
aniversario = input("Digite seu aniversário (DDMMAAAA): ")

# Verifica se a entrada do usuário é composta apenas por dígitos.
if aniversario.isdigit():
    # Verifica se o aniversário está nos dígitos de π.
    if aniversario in pi_decimals_only:
        print("Seu aniversário está em π!")
    else:
        print("Seu aniversário não está em π.")
else:
    print("Por favor, digite uma data em formato numérico válido (DDMMAAAA).")

# Nota: A busca é feita nos dígitos decimais de π, excluindo o '3.' inicial.
