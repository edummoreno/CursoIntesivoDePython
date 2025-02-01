from pathlib import Path

# Define o caminho para o arquivo 'python.txt'
path = Path('python.txt')

# Escreve uma string inicial no arquivo, se ele ainda não existir ou se quisermos sobrescrever.
path.write_text("Eu gosto muito de programar.\n", encoding='utf-8')

# Inicializa a variável de conteúdo e o contador
contents = ''
contador = 1

# Loop que repete a operação de concatenação de texto 1.000.000 de vezes
while contador <= 1.000000:
    # A cada iteração, adiciona a string desejada ao conteúdo
    contents += f"Vou me tornar um especialista em Python e Inteligência Artificial, não apenas um especialista! {contador}\n"
    contador += 1

# Escreve o conteúdo acumulado no arquivo, no final do texto já existente.
# Utiliza o método 'open' com o modo 'a' para anexar o texto, em vez de sobrescrever.
with path.open('a', encoding='utf-8') as file:
    file.write(contents)

print("Arquivo pronto! O texto foi adicionado com sucesso.")
