from pathlib import Path

# Define o caminho para o arquivo 'pi_digits.txt'. Assume-se que o arquivo está no mesmo diretório que o script.
# Se estiver em outro diretório, deve-se fornecer o caminho relativo ou absoluto correto.
path = Path('pi_digits.txt')

try:
    # Lê o conteúdo do arquivo e já remove espaços em branco à direita usando o encadeamento de métodos.
    contents = path.read_text(encoding='utf-8').rstrip()
except FileNotFoundError:
    # Se o arquivo não for encontrado, informa ao usuário.
    print(f"O arquivo {path} não foi encontrado. Verifique se o nome e o caminho estão corretos.")
except Exception as e:
    # Se ocorrer qualquer outro tipo de exceção, exibe a mensagem de erro.
    print(f"Ocorreu um erro ao ler o arquivo {path}: {e}")
else:
    # Se a leitura for bem-sucedida, imprime o conteúdo do arquivo.
    print(f"Conteúdo do arquivo {path}:")
    print(contents)
