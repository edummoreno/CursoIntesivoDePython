from mpmath import mp


# configura a precisao desejada. O mpmath permite definir a precisão em 'dps' (dígitos de precisão).
mp.dps = 1000000 #O mpmath permite definir a precisão em 'dps' (dígitos de precisão).O mpmath permite definir a precisão em 'dps' (dígitos de precisão).

# Calcula pi com precisão configurada
pi_calculated = mp.pi

#converte o valor de pi para uma string.
pi_string = str(pi_calculated)

with open('pi_milhao_decimais.txt','w') as file:
    file.write(pi_string)

# Escreve o valor de pi no arquivo.
print("Arquivo com 1 milhao de casa decimais foi criado")