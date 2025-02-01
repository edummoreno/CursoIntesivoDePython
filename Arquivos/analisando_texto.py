from pathlib import Path

#corrigir, só está funcionando com caminho absoluto
path = Path('alice.txt')

#utilizar os metodos
try:
    conteudo = path.read_text(encoding='utf-8')

except:
    print(f"Desculpe o arquivo {path} nao foi encontrado")
else:
    #conta o numero aproximado de palavras no arquivo
    palavra = conteudo.split()
    num_words = len(palavra)
    print(f"O Arquivo {path} tem cerca de {num_words} palavras")
