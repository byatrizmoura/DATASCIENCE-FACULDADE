'''
COLEÇÕES
- LISTAS
- TUPLAS
- DICIONARIOS
'''

#LISTAS
# semelhante ao array em outras linguagens
# são sequencias mutaveis de n valores de qualquer tipo (inclusive de outras coleçoes). Podem ser entendidas como um vetor de elementos.
# possivel criar uma lista vazia. ex.: lista_vazia = []   a = []

a = "Apostila de Python é top!"
#Converter cada letra em lista: list()
b = list(a)
print(b)
#Converter por espaços ou lementos previamente indicados: .split()
c = a.split()
print(c)
#reverter uma lista em string: join() / junta com base em algum delimitador
d = " ".join(c)
print(d)

#exemplo
amigos = ["Joao","Luiz","Julia","Fabio","Lucas"]
amigos[1] = "Silvana" #subistitui item em determinada posiçao da lista
print(amigos)
amigos.append("Marcio") #inclui o item a lista
print(amigos)
amigos.remove("Julia") #remove o item informado
print(amigos)
amigos.pop(3) #remove o item na posiçao informada
print(amigos)
#print(amigos[1:3]) seleciona intervalo
#print(amigos[2:])  seleciona intervalo daquele item até o fim
#print(amigos[-1])  tambem pode ser selecionado de tras para frente

#faz a ordeenaçao da lista
numeros = [10,9,20,40,35,66]
numeros.sort()
print(numeros)

#TUPLAS
#Tuplas são imutáveis, ou seja, não é possivel realizar alteraçoes em tuplas criadas como fazemos com listas.
#parenteses são opcionais, mas em tuplas se usa partenteses() e em listas conchetes[]
#é possivel converter listas em tuplas e vice versa
lista = [0,1,2,3]
tupla = tuple(lista)
print(tupla)

liista = list(tupla)
print(liista)

#DICIONARIOS  -- MAIS UTILIZADA
#COMPOSTO DE CHAVE E VALOR, SENDO AS CHAVES IMUTÁVEIS E OS VALORES MUTAVEIS
#Se diz que uma PROPRIEDADE é composta de uma chave e um valor

dicionario = {"chave1":1, "chave2":2, "chave3":3}
#del dicionario ["chave1"]  #deleta uma chave
print(dicionario)
print("chave2" in dicionario) #verifica se possui essa chave no dicionario
print(dicionario.items()) #mostra todos os itens do dicionario
print(dicionario.values()) #mostra somente os valores
print(dicionario.keys())  #mostra somente as chaves
print(len(dicionario))  #funçao builtin - retorna o tamanho da lista (neste caso, numero de chaves)

"""
dicionario = dict()
dicionario["chave1"] = 1
dicionario["chave2"] = 2
dicionario["chave3"] = 3  #adiciona elementos
print(dicionario)
"""

#exemplo
aluno ={"nome" : "Lucas", "idade" : 29, "conceito" : "A"}
print(aluno)
print(aluno["nome"])
aluno.update({"nome":"Antonio", "conceito" : "B"})
print(aluno)
aluno.update({"endereco":"Rua dos Andradas"})
print(aluno)

del aluno["idade"]
print(aluno)

#itear
for x in aluno: #mostra todas as chaves do dicionario
    print(x)

for x in aluno.values(): #mostra todas os valores do dicionario
    print(x)

for x in aluno.items(): #mostra todas os itens do dicionario
    print(x)

for keys,values in aluno.items(): #mostra todas as chaves e valores do dicionario
    print(keys , values)

###################

#ARRAY
# o Python não tem array nativo, sendo assim sera necessário importar
import array as ary
#a = ary.array("d",[1.1,1.2,1.3,1.4,1.5])
#print(a)

lista = [1.1,1.2,1.3,1.4]
lista1 = [2.1,2.2,2.3,2.4]
a = ary.array("d", lista)
print(a[1])  #acessar um elemento
print(a[1:3])  #acessar um intervalo de elementos  ou 1: para acessar de um determ. item até o fim ou -2 para acessar de tras para frente
a[0] = 1.8  #altera item
a.append(1.6)  #acrescenta item
print(a)
a.extend([1.5, 1.9, 1.1]) #acrescenta varios itens
print(a)
numbers = lista + lista1
print(numbers)
del lista1[2]
print(lista1)
tamanho = len(lista1)
print(tamanho)

##############

#CONJUNTO
# faz algumas operaçoes, como uniao, diferença, soma
s ={"aa", "ab", "ac"}

s.add("ad")
print(s)

s.update("1", "2", "3")
print(s)
"""
s.remove("ac")
print(s)
"""

u = {"A","B","C","D","E","F","G"}
t = {"F", "G", "H"}
novo = s.union(t)
print(novo)

novo2 = u - t  #traz a diferença, o que tem somente no u
print(novo2)

novo2 = u & t  #traz a interceçao, o que tem em comum em u e t
print(novo2)

novo2 = u ^ t  #traz a diferença simetrica, elementos que não são comuns em u e t
print(novo2)

for i in u:
    print(i)