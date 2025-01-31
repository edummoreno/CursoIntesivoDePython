class Dog:
    """Uma simples tentativa de modelar um cachorro."""
    # A docstring acima descreve a finalidade da classe Dog.

    def __init__(self, name, age):
        """
        Inicializa os atributos de nome e idade.
        Este é o método construtor que é chamado quando um novo objeto Dog é criado.
        """
        self.name = name  # Atributo que armazena o nome do cachorro.
        self.age = age    # Atributo que armazena a idade do cachorro.

    def sit(self):
        """
        Simula um cachorro sentando em resposta a um comando.
        Este é um método que imprime uma mensagem indicando que o cachorro está sentando.
        """
        print(f"{self.name} is now sitting.")  # Mensagem formatada com o nome do cachorro.

    def roll_over(self):
        """
        Simula um cachorro rolando em resposta a um comando.
        Este é um método que imprime uma mensagem indicando que o cachorro rolou.
        """
        print(f"{self.name} rolled over!")  # Mensagem formatada com o nome do cachorro.

# Criação da instância da classe Dog, com o nome 'willie' e a idade 6.
my_dog = Dog('willie', 6)

# Utilizando os atributos name e age do objeto my_dog.
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
