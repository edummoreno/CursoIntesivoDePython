from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().lstrip()

lines = contents.splitlines()
pi_string = '' #define variavel antes só em casos que ele aponta erro.
for line in lines:
    pi_string += line #soma as linhas


print(pi_string)
print(len(pi_string))