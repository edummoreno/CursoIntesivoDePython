from mpmath import mp

# Configura a precisão desejada. O mpmath permite definir a precisão em 'dps' (dígitos de precisão).
# Aqui estamos configurando para 1 milhão de dígitos de precisão.
mp.dps = 1000000

# Calcula π com a precisão configurada.
pi_calculated = mp.pi

# Converte o valor de π para uma string.
# A string incluirá o dígito '3' e o ponto decimal, além dos dígitos decimais.
pi_string = str(pi_calculated)

# Tenta escrever o valor de π no arquivo.
try:
    with open('pi_milhao_decimais.txt', 'w', encoding='utf-8') as file:
        file.write(pi_string)
except IOError as e:
    # Informa ao usuário se ocorrer um erro de E/S (entrada/saída), como problemas de escrita no arquivo.
    print(f"Ocorreu um erro ao escrever o arquivo: {e}")
else:
    # Se a escrita for bem-sucedida, informa ao usuário.
    print("Arquivo com 1 milhão de casas decimais de π foi criado com sucesso.")
