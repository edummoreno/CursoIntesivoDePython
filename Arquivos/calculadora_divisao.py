# Calculadora de divisão simples com tratamento de erro usando try/except

print("Dê dois números para fazer a divisão.")
print("Enter 'q' para sair a qualquer momento.")

while True:
    # Solicita ao usuário para inserir o primeiro número
    primeiro_numero = input("\nPrimeiro Número: ")
    if primeiro_numero.lower() == 'q':  # Verifica se o usuário quer sair
        break

    # Solicita ao usuário para inserir o segundo número
    segundo_numero = input("\nSegundo Número: ")
    if segundo_numero.lower() == 'q':  # Verifica se o usuário quer sair
        break

    try:
        # Tenta converter as entradas para float, para permitir números decimais, e realizar a divisão
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        resposta = primeiro_numero_float / segundo_numero_float
    except ValueError:
        # Captura o erro caso a entrada não possa ser convertida para um número
        print("Entrada inválida. Por favor, insira um número válido ou 'q' para sair.")
    except ZeroDivisionError:
        # Captura o erro caso o segundo número seja zero
        print("Erro: Não é possível dividir por zero.")
    except Exception as e:
        # Captura qualquer outro tipo de exceção e imprime a mensagem de erro
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        # Se a divisão for bem-sucedida, imprime o resultado
        print(f"\n{primeiro_numero_float} dividido por {segundo_numero_float} é {resposta}")

print("Calculadora encerrada.")
