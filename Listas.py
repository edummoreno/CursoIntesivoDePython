import string

bikes = ['caloi','eletrica','com marcha']

print(bikes)
print(bikes[0])
print(bikes[0].title())
print(bikes[-1])

nome = ['Eduardo','João','Jesus']

print("Bem vindo ",nome[0])
print("Bem vindo ",nome[1])
print("Bem vindo ",nome[2])

#modificando lista

moto = ['yamaha','honda','nike']

moto[2] = 'toyota'

print(moto[2])

#adicionando

moto.append('ducati')

print(moto[3])

#inserindo 

moto.insert(1,'mistubishi')

print(moto[1])

#deletando
del moto[1]

print(moto)

#removendo com pop() #remove o ultmo item da lista 
pop_moto = moto.pop() # salva o item removido

print(moto)
print(pop_moto)

#qualquer posiçao
pop_moto = moto.pop(0)
print(pop_moto)

#removendo elemento por valor
#remove_moto = moto.remove('ducati')

#print(remove_moto)  #revisar

#ordenando listas

cars = ['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars))
cars.sort()
print(cars)

cars.reverse()
print(cars)

#evitando erros ao trabalhar com listas
#sempre olhe o tamanho de uma lista para verificar os indices corretos, lembrese que o indice começa no 0 
# indice[-1] exibe o ultimo item de uma lista
print(len(cars))


