#calculadora

print("Digite 'q' para sair ")

while True:
    numero_1 = float(input("Digite um numero: "))
    if numero_1 == 'q':
        break
    operador = input("Digite Soma, Substração, multiplicação, ou divisão: ")
    numero_2 = float(input("Digite um numero: "))

    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == '-':
        resultado = numero_1 - numero_2
    elif operador == '*':
        resultado = numero_1 * numero_2
    elif operador == '/':
        resultado = numero_1 / numero_2
    else:
        print("Invalido!")

    print(f"o Resultado é {resultado}")