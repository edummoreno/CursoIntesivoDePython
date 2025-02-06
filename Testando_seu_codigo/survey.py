class AnonymousSurvey:
    """Coleta respostas anônimas para uma pergunta da pesquisa"""

    def __init__(self, question):
        """Armazena uma pergunta e prepare para armazenar respostas"""
        self.question = question
        self.responses = []

    def show_question(self):
        """mostra a pergunta da pesquisa"""
        print(self.question)


    def store_response(self, new_response):
        """Armazena uma unica resposta a pesquisa"""
        self.responses.append(new_response)

    def show_results(self):
        """mostra todas as respostas fornecidas"""
        print("Survey results:")
        for response in self.responses:
            print(f" - {response}")

