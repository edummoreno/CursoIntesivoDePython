from pathlib import Path

def conta_palavra(path):
    """
    Conta o número aproximado de palavras em um arquivo especificado pelo caminho 'path'.
    
    :param path: Path - O caminho para o arquivo a ser lido.
    """
    try:
        # Tenta ler o conteúdo do arquivo com a codificação UTF-8.
        conteudo = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Informa ao usuário se o arquivo especificado pelo caminho não for encontrado.
        print(f"Desculpe, o arquivo {path} não foi encontrado.")
    except Exception as e:
        # Informa ao usuário sobre qualquer outro tipo de exceção que ocorra.
        print(f"Ocorreu um erro ao processar o arquivo {path}: {e}")
    else:
        # Conta o número de palavras no arquivo.
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print(f"O arquivo {path} tem cerca de {num_palavras} palavras.")

# Lista de nomes de arquivos para processar.
# Corrigido o nome do terceiro arquivo, removendo a vírgula.
nomes_arquivos = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']

# Percorre cada nome de arquivo na lista e chama a função para contar palavras.
for nome_arquivo in nomes_arquivos:
    caminho = Path(nome_arquivo)
    conta_palavra(caminho)
