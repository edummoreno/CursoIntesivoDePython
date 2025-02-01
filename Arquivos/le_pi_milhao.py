from pathlib import Path

path = Path('pi_milhao_decimais.txt')
contents = path.read_text()

lines = contents = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))