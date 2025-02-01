from pathlib import Path

# Define o caminho para o arquivo 'pi_digits.txt'.
# Assume-se que o arquivo está no mesmo diretório que o script.
# Se estiver em outro diretório, forneça o caminho relativo ou absoluto.
path = Path('pi_digits.txt')

try:
    # Tenta ler o conteúdo do arquivo e já remove espaços em branco à esquerda.
    contents = path.read_text(encoding='utf-8').lstrip()
except FileNotFoundError:
    # Informa ao usuário se o arquivo não for encontrado.
    print(f"O arquivo {path} não foi encontrado. Verifique se o nome e o caminho estão corretos.")
except Exception as e:
    # Exibe uma mensagem de erro para qualquer outra exceção ocorrida.
    print(f"Ocorreu um erro ao ler o arquivo {path}: {e}")
else:
    # Se a leitura for bem-sucedida, divide o conteúdo em linhas.
    lines = contents.splitlines()
    
    # Inicializa uma string para acumular os dígitos de pi.
    pi_string = ''
    
    # Percorre cada linha e adiciona à string de pi.
    for line in lines:
        pi_string += line  # Aqui, não usamos lstrip(), pois queremos manter o conteúdo de cada linha como está.
    
    # Imprime a string de dígitos de pi.
    print(f"Os dígitos de pi lidos do arquivo são: {pi_string}")
    
    # Imprime o comprimento total da string de pi.
    print(f"O total de dígitos de pi lidos é: {len(pi_string)}")
