from pathlib import Path

# Define o caminho para o arquivo 'pi_milhao_decimais.txt'.
# Assume-se que o arquivo está no mesmo diretório que o script.
# Caso contrário, forneça o caminho relativo ou absoluto adequado.
path = Path('pi_milhao_decimais.txt')

try:
    # Tenta ler o conteúdo do arquivo com a codificação UTF-8.
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # Informa ao usuário se o arquivo não for encontrado.
    print(f"O arquivo {path} não foi encontrado. Verifique se o nome e o caminho estão corretos.")
except Exception as e:
    # Exibe uma mensagem de erro para qualquer outra exceção ocorrida.
    print(f"Ocorreu um erro ao ler o arquivo {path}: {e}")
else:
    # Divide o conteúdo do arquivo em linhas.
    lines = contents.splitlines()
    
    # Inicializa uma string para acumular os dígitos de pi.
    pi_string = ''
    
    # Percorre cada linha, remove espaços em branco à esquerda e adiciona à string de pi.
    for line in lines:
        pi_string += line.lstrip()
    
    # Imprime os primeiros 52 dígitos de pi seguidos de reticências.
    print(f"Os primeiros 52 dígitos de pi são: {pi_string[:52]}...")
    
    # Imprime o comprimento total da string de pi, ou seja, o total de dígitos lidos.
    print(f"O total de dígitos de pi lidos é: {len(pi_string)}")
