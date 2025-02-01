from pathlib import Path

# Tenta ler o arquivo 'alice.txt' a partir do diretório atual
# Se o arquivo não estiver no diretório atual, o caminho deve ser especificado
try:
    # Cria um objeto Path com o nome do arquivo
    path = Path('alice.txt')
    
    # Lê o conteúdo do arquivo, especificando a codificação para evitar problemas com caracteres especiais
    conteudo = path.read_text(encoding='utf-8')

except FileNotFoundError:
    # Se ocorrer um erro de arquivo não encontrado, informa ao usuário
    print(f"Desculpe, o arquivo {path} não foi encontrado.")
else:
    # Se a leitura for bem-sucedida, processa o conteúdo
    
    # Divide o conteúdo do arquivo em uma lista de palavras
    palavras = conteudo.split()
    
    # Calcula o número de palavras na lista
    num_palavras = len(palavras)
    
    # Imprime o resultado com o número aproximado de palavras no arquivo
    print(f"O arquivo {path} tem cerca de {num_palavras} palavras.")
