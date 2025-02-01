from pathlib import Path

# Cria um objeto Path com o nome do arquivo. Se o arquivo estiver no mesmo diretório,
# o caminho relativo é simplesmente o nome do arquivo.
path = Path('pi_digits.txt')

# Lê o conteúdo do arquivo e armazena na variável contents.
#contents = path.read_text()

# Remove qualquer espaço em branco do lado direito do conteúdo lido.
#contents = contents.rstrip()

#encadeamento de metodos
contents = path.read_text().rstrip()

# Imprime o conteúdo do arquivo sem os espaços em branco à direita.
print(contents)
