from pathlib import Path

# Define o caminho para o arquivo 'pi_digits.txt'. Assume-se que o arquivo está no mesmo diretório que o script.
# Se estiver em outro diretório, deve-se fornecer o caminho relativo ou absoluto.
path = Path('pi_digits.txt')

try:
    # Tenta ler o conteúdo do arquivo.
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # Se o arquivo não for encontrado, informa ao usuário.
    print(f"O arquivo {path} não foi encontrado. Verifique se o nome e o caminho estão corretos.")
except Exception as e:
    # Se ocorrer qualquer outro tipo de exceção, exibe a mensagem de erro.
    print(f"Ocorreu um erro ao ler o arquivo {path}: {e}")
else:
    # Se a leitura for bem-sucedida, divide o conteúdo em linhas e imprime cada uma.
    lines = contents.splitlines()
    for line in lines:
        print(line)
