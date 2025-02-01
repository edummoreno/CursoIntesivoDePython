from mpmath import mp


# configura a precisao desejada. O mpmath permite definir a precisão em 'dps' (dígitos de precisão).
mp.dps = 1000000 #O mpmath permite definir a precisão em 'dps' (dígitos de precisão).O mpmath permite definir a precisão em 'dps' (dígitos de precisão).

# Calcula pi com precisão configurada
pi_calculated = mp.pi

#converte o valor de pi para uma string.
pi_string = str(pi_calculated)


aniversario = input("Digite seu aniversario: ")
if aniversario in pi_string:
    print("seu aniversario está em pi")
else:
    print("ser aniversario não está em pi")