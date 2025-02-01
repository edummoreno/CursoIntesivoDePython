# Calculadora de divisão simples com tratamento de erro usando try/except

while True:
    # Solicita ao usuário para inserir o primeiro número
    primeiro_numero = input("\nPrimeiro número: ")
    if primeiro_numero.lower() == 'q':  # Verifica se o usuário quer sair
        break

    # Solicita ao usuário para inserir o segundo número
    segundo_numero = input("\nSegundo número: ")
    if segundo_numero.lower() == 'q':  # Verifica se o usuário quer sair
        break

    try:
        # Tenta converter as entradas para inteiros e realizar a divisão
        primeiro_numero_int = int(primeiro_numero)
        segundo_numero_int = int(segundo_numero)
        resposta = primeiro_numero_int / segundo_numero_int
    except ValueError:
        # Captura o erro caso a entrada não possa ser convertida para um inteiro
        print("Você deve inserir um número válido ou 'q' para sair.")
    except ZeroDivisionError:
        # Captura o erro caso o segundo número seja zero
        print("Não é possível dividir por zero.")
    except Exception as e:
        # Captura qualquer outro tipo de exceção e imprime a mensagem de erro
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        # Se a divisão for bem-sucedida, imprime o resultado
        print(f"\n{primeiro_numero_int} dividido por {segundo_numero_int} é {resposta}")

print("Calculadora encerrada.")
