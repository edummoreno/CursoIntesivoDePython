from pathlib import Path

path = Path('python.txt')
path.write_text("Eu Gosto Muito de Programar.")

contents = ''
contador = 1

while contador <= 1000000:
    contents += "Vou me tornar um especialista em python e Inteligência Artifical, não mais que um especialista!"
    contador += 1
    
path.write_text(contents)

print("Arquivo Pronto!")