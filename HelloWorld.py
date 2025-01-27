import string
import this

menssagem = "Hello World!!! faz o que da! melhor feito do que bem feito! - lembre-se crtl shit p"
print(menssagem.title())
print(menssagem.upper())
print(menssagem.lower())

Primeiro_nome = "Eduardo"
Segundo_nome = "Moreno Neto"

nome_completo = f"{Primeiro_nome} {Segundo_nome}"

print("\t"+nome_completo)

#removendo espaço em branco

espaco = "    python    "

print(espaco.strip())
print(espaco.rstrip())
print(espaco.lstrip())

#removendo prefixo

site = "https://google.com.br"

site = site.removeprefix('https://')

print(site)

site = site.removesuffix('.br')

print(site)

#inteiro

numero = 2 * 3
print(numero)

#float
numero_float = 0.5 * 6
print(numero_float)

#underscore

undescore = 14_000_000_000
print(undescore)

#atribuição multipla

a,b,c = "a","b","c"

print(a + b + c)

#The Zen of Python, by Tim Peters

#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!


