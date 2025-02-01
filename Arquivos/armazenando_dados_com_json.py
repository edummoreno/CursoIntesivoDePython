from pathlib import Path
import json

#lista
numeros = [2,3,5,7,11,13]

#variavel recebe caminho do numeros.json
caminho = Path('numeros.json')

#para criar um json utilize o metodo json.dumps()
conteudo = json.dumps(numeros)

#para criar um arquivo utilize o metodo write_text()
caminho.write_text(conteudo)
