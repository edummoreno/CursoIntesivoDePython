from mpmath import mp

# Configura a precisão desejada. O mpmath permite definir a precisão em 'dps' (dígitos de precisão).
# Aqui estamos configurando para 1 bilhão de dígitos de precisão.
mp.dps = 1000000000

# Calcula pi com a precisão configurada.
pi_calculated = mp.pi

# Converte o valor de pi para uma string.
pi_string = str(pi_calculated)

# Tenta escrever o valor de pi no arquivo.
try:
    with open('pi_bilhao_decimais.txt', 'w', encoding='utf-8') as file:
        file.write(pi_string)
except IOError as e:
    # Informa ao usuário se ocorrer um erro de E/S (entrada/saída), como problemas de escrita no arquivo.
    print(f"Ocorreu um erro ao escrever o arquivo: {e}")
else:
    # Se a escrita for bem-sucedida, informa ao usuário.
    print("Arquivo com 1 bilhão de casas decimais de pi foi criado com sucesso.")

# Nota: O valor de pi calculado pelo mpmath pode incluir um prefixo '3.' na string.
# Se você deseja apenas os dígitos após o ponto decimal, você pode ajustar a string de acordo.
