#utilizando o try except em um caso onde não é possivel executar o código.



numero_zero = (0)
numero_um = (1)

try:
    divisao_por_zero = numero_um / numero_zero
except:
    print("Matematicamente não é possivel dividir por zero")


try:
    print(divisao_por_zero)
except:
    print("Nao tem nada na variavel pois não é possivel dividir por zero")
