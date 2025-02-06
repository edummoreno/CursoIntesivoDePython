from survey import AnonymousSurvey

# Esse programa realiza uma pesquisa anônima. Veja abaixo a explicação de cada elemento:

# Classe:
#   - 'AnonymousSurvey' é uma classe, ou seja, um modelo que define os atributos (dados) e métodos (funções)
#     que os objetos da pesquisa terão. Ela encapsula a lógica para coletar e exibir respostas.
#
# Objeto:
#   - Um objeto é uma instância de uma classe. Aqui, 'language_survey' é um objeto criado a partir
#     da classe 'AnonymousSurvey'. Esse objeto possui seus próprios atributos (como a pergunta e as respostas)
#     e pode utilizar os métodos definidos na classe.
#
# Instanciação:
#   - Instanciação é o processo de criar um objeto a partir de uma classe. Ao chamar 'AnonymousSurvey(question)',
#     estamos instanciando a classe, ou seja, criando o objeto 'language_survey' com a pergunta especificada.
#
# Método:
#   - Um método é uma função definida dentro de uma classe. Métodos como 'show_question()', 'store_response()'
#     e 'show_results()' pertencem à classe 'AnonymousSurvey' e operam sobre os objetos dessa classe.
#
# Função:
#   - Uma função é um bloco de código que realiza uma tarefa específica. Em Python, funções definidas
#     fora de uma classe são funções comuns, mas quando definidas dentro de uma classe, elas são chamadas de métodos.
#
# -------------------------------------------------------------------------------

# Define a pergunta da pesquisa:
question = "What language did you first learn to speak?"

# Instanciação: cria um objeto 'language_survey' a partir da classe 'AnonymousSurvey'
language_survey = AnonymousSurvey(question)  # 'language_survey' é o objeto que armazena a pergunta e as respostas

# Chamada de método: 'show_question()' é um método (função da classe) que exibe a pergunta armazenada
language_survey.show_question()

print("Enter 'q' at any time to quit.\n")

# Loop para coletar as respostas do usuário:
while True:
    response = input("Language: ")
    if response == 'q':
        break
    # Chamada do método 'store_response()' que armazena cada resposta fornecida pelo usuário
    language_survey.store_response(response)

# Exibe os resultados da pesquisa:
print("\nThank you to everyone who participated in the survey!")
# Chamada do método 'show_results()' que exibe todas as respostas coletadas
language_survey.show_results()
