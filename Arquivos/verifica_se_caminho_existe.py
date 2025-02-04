from pathlib import Path
import json


try:
    caminho = Path.exists('username.json')
except:
    print("Caminho não encontrado")

try:    
    if caminho.exists():
        conteudo = caminho.read_text()
        username = json.loads(conteudo)
        print(f"Bem-Vindo, {username}")
    else:
        username = input("Qual seu nome? ")
        conteudo = json.dumps(username)
        caminho.write_text(conteudo)
        print(f"{username} seu nome foi guardado")
except:
    print("Caminho não encontrado")
