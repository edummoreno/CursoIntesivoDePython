from pathlib import Path
import json

# Pede ao usuário para inserir seu nome.
username = input("Qual o seu nome? ")

# Define o caminho para o arquivo onde o nome será salvo.
caminho = Path('username.json')

try:
    # Tenta escrever a string JSON do nome do usuário no arquivo.
    # A função 'dumps' converte um objeto Python em uma string JSON.
    conteudo = json.dumps(username)
    caminho.write_text(conteudo, encoding='utf-8')  # Correção: o método 'write_text' é usado diretamente no objeto Path.
except Exception as e:
    # Informa ao usuário se ocorreu algum erro durante a escrita do arquivo.
    print(f"Ocorreu um erro ao salvar seu nome: {e}")
else:
    # Se a escrita for bem-sucedida, informa ao usuário que o nome foi salvo.
    print(f"Lembraremos de você quando voltar, {username}!")

# Carrega o nome do usuário do arquivo e imprime, se disponível.
try:
    # Tenta ler o conteúdo do arquivo.
    conteudo_lido = caminho.read_text(encoding='utf-8')
    # Converte a string JSON de volta para um objeto Python (neste caso, uma string).
    nome_salvo = json.loads(conteudo_lido)
    print(f"Seu nome salvo é: {nome_salvo}")
except FileNotFoundError:
    # Informa ao usuário se o arquivo não for encontrado.
    print("O arquivo com seu nome não foi encontrado.")
except json.JSONDecodeError:
    # Informa ao usuário se houver um erro ao decodificar a string JSON.
    print("Ocorreu um erro ao decodificar o nome salvo no arquivo.")
except Exception as e:
    # Informa ao usuário sobre qualquer outro tipo de exceção.
    print(f"Ocorreu um erro inesperado: {e}")
