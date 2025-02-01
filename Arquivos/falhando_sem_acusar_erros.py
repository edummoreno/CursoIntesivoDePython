from pathlib import Path


def conta_palavra(path):
    try:
        conteudo = path.read_text(encoding='utf-8')

    except:
        pass
    else:
        #conta o numero aproximado de palavras no arquivo
        palavra = conteudo.split()
        num_words = len(palavra)
        print(f"O Arquivo {path} tem cerca de {num_words} palavras")


#corrigir, só está funcionando com caminho absoluto
nomeArquivos = ['alice.txt','siddhartha.txt','mody_dusk,txt']

for nomeArquivo  in nomeArquivos:
    caminho = Path(nomeArquivo)
    conta_palavra(caminho)