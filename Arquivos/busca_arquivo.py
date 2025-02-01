from pathlib import Path

def buscar_arquivo(diretorio, nome_arquivo):
    """
    Busca recursivamente por um arquivo em um diretório e seus subdiretórios.
    
    :param diretorio: Path - O diretório onde começar a busca.
    :param nome_arquivo: str - O nome do arquivo a ser encontrado.
    :return: Path ou None - O caminho do arquivo se encontrado, caso contrário None.
    """
    # Verifica se o diretório fornecido existe
    if not diretorio.exists():
        print(f"O diretório {diretorio} não existe.")
        return None
    
    # Percorre todos os itens no diretório
    for item in diretorio.iterdir():
        # Se o item é um arquivo e corresponde ao nome procurado, retorna o caminho do arquivo
        if item.is_file() and item.name == nome_arquivo:
            return item
        # Se o item é um diretório, chama a função de busca recursivamente
        elif item.is_dir():
            resultado = buscar_arquivo(item, nome_arquivo)
            # Se o arquivo foi encontrado em um subdiretório, retorna o caminho
            if resultado:
                return resultado
    
    # Se o arquivo não foi encontrado após percorrer o diretório e seus subdiretórios, retorna None
    return None

# Define o diretório inicial da busca
diretorio_inicial = Path('.')

# Nome do arquivo que estamos procurando
nome_arquivo_procurado = 'alice.txt'

# Inicia a busca pelo arquivo
arquivo_encontrado = buscar_arquivo(diretorio_inicial, nome_arquivo_procurado)

# Verifica se o arquivo foi encontrado e imprime o resultado
if arquivo_encontrado:
    print(f"O arquivo {nome_arquivo_procurado} foi encontrado em: {arquivo_encontrado}")
else:
    print(f"O arquivo {nome_arquivo_procurado} não foi encontrado no diretório e subdiretórios.")
