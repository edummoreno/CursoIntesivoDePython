from pathlib import Path

# Define o caminho para o arquivo 'alice.txt'. Se estiver no mesmo diretório, isso funciona bem.
# Caso contrário, você deve fornecer o caminho relativo ou absoluto.
path = Path('alice.txt')

try:
    # Tenta ler o conteúdo do arquivo no formato de texto, com codificação UTF-8.
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # Se o arquivo não for encontrado, imprime uma mensagem de erro específica.
    print("Arquivo não encontrado.")
else:
    # Se a leitura for bem-sucedida, você pode processar o conteúdo aqui.
    # Por exemplo, vamos imprimir o conteúdo do arquivo.
    print(contents)
