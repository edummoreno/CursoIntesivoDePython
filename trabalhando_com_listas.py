import this

magica = ['magico de oz','alice','harry potter']

#loop for com lista

for magi in magica:
    print(magi)

#prestar atenção nos erros de identação, não esquecer os dois pontos : 

#utilizando função range

for value in range(1,6): #utilizar sempre um a mais para o range, ex: 5 o range vai até 6
    print(value)

#criando lista com range

num = list(range(1,6))
print(num)


#numeros pares e imapr em uma lista com range

par_num = list(range(2,11,2))
print(par_num)
impar_num = list(range(1,13,2))
print(impar_num)

#numeros ao quadrado

quadrados = []
for value in range(1,11):
    quadrado = value ** 2
    quadrados.append(quadrado)

print(quadrados)

#estatistica simples com numeros inteiros

lista_estatistica = []
for val in range(1,11):
    lista_estatistica.append(val)

print(lista_estatistica)

print(min(lista_estatistica))
print(max(lista_estatistica))
print(sum(lista_estatistica))


#listas comprimidas # gerar lista com apenas uma linha de código

quadrado = [val**2 for val in range(1,11)]
print(quadrado)

#fatiando lista

alfabeto = ['a','b','c','d','f','g','h','i','j']

print(alfabeto[0:3])
print(alfabeto[:4])
print(alfabeto[2:])


#percorrendo list com loop

for letra in alfabeto[:3]:
    print(letra.title())


#copiando um lista
copia_alfabeto = alfabeto[:]

print(copia_alfabeto)