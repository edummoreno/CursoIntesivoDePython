from pathlib import Path
import json

# Lista de números primos
numeros = [2, 3, 5, 7, 11, 13]

# Criando um objeto Path para o arquivo 'numeros.json'
caminho_arquivo = Path('numeros.json')

# Serializando a lista para um formato JSON legível
conteudo_json = json.dumps(numeros, indent=4)  # O parâmetro 'indent' melhora a legibilidade do JSON

# Escrevendo o conteúdo JSON no arquivo
caminho_arquivo.write_text(conteudo_json)

print(f"Os números foram salvos com sucesso em {caminho_arquivo}")
