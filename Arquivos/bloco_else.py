#continuação da calculadora
print("me de dois numeros, para fazer a divisão")
print("Enter 'q' para sair")


#calculadora de divisão simples utilizando try except para tratamento de erro

while True:
    primeiro_numero = int(input("\nPrimeiro Numero:"))
    if primeiro_numero == 'q':
        break

    segundo_numero = int(input("\nSegundo Numero: "))
    if segundo_numero == 'q':
        break

    try:
        resposta = primeiro_numero / segundo_numero
    except:
        print("nao foi possivel realizar essa divisao")
    else:
        print(f"\n {primeiro_numero} dividido por {segundo_numero} é {resposta}")
