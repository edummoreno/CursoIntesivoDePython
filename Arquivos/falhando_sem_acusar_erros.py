from pathlib import Path

def conta_palavra(path):
    """
    Conta o número aproximado de palavras em um arquivo especificado pelo caminho 'path'.
    
    :param path: Path - O caminho para o arquivo a ser lido.
    """
    try:
        # Tenta ler o conteúdo do arquivo com a codificação UTF-8
        conteudo = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Se o arquivo não for encontrado, imprime uma mensagem de erro e ignora o arquivo
        print(f"O arquivo {path} não foi encontrado. Verifique se o nome está correto e tente novamente.")
    except Exception as e:
        # Se ocorrer qualquer outra exceção, imprime a mensagem de erro
        print(f"Ocorreu um erro ao ler o arquivo {path}: {e}")
    else:
        # Se a leitura for bem-sucedida, prossegue para contar as palavras
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print(f"O arquivo {path} tem cerca de {num_palavras} palavras.")

# Lista de nomes de arquivos para processar
nomes_arquivos = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']  # Corrigido o nome do arquivo 'mody_dusk,txt'

# Percorre cada nome de arquivo na lista
for nome_arquivo in nomes_arquivos:
    caminho = Path(nome_arquivo)
    conta_palavra(caminho)
