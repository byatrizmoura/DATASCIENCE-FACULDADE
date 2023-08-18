#CONDICIONAIS IF, ELIF, ELSE
x = 4
y = 5
if y > x:
    print(" y is a larger number than x ")
else:
    print(" y is a smaller number than x ")
#OBS.: Em python 0 é apresentado para uma condiçao False e 1 para True

#elif - permite que você verifique de uma outra forma
x = 10
y = 11
if x < y:
    print("x is smaller ")
elif y > y:
    print(" y is smaller ")
else:
    print("x and y are equal")

#FOR

#loop for pega uma sequencia e executa um trecho de codigo para cada item daquela sequencia/grupo

numbers = [10,23,43,54,65,64,87,43,21,11]
for number in numbers:
    print(number)

#inline fazendo o exponencial por 2 de cada item
numbers = [10,23,43,54,65,64,87,43,21,11]
print([number**2 for number in numbers])

#funçao range(10) incrementa uma sequencia que vai do 0 ao 9
for i in range(10):
    print(i)
#pode alterar a esse padrão dizendo que a sequencia inicia em x e vai ate y, ex.:
for i in range(3,10):
    print(i)
#pode alterar a esse padrão acrescentando um parametro no terceiro item, a sequencia inicia em x e vai ate y, pulando de 2 em 2, ex.:
for i in range(3,10, 2):
    print(i)

#instruçao continue = retorna o interpretador ao inicio do loop e executa proximo ciclo
numbers = [ 12, 34, 23, 46, 45, 77, 65, 98, 53, 21 ]
for number in numbers:
    if number%2 ==0: #numero dividido por 2 igual a 0, ou seja, for divisivel/modulo de 2
        continue
    print(number)

#for - instruçao else
for i in range(1,100,2):
    print(i)
else:
    print('Reached to the limit')

#instruçao break
for i in range(1,100,2):
    print(i)
    if i ==26:
        break
else:
    print('Reached to the limit')

#exemplo: uma regra de negócio onde so poderia efetuar 3 tentativas de compra
flagcompra = True
info = "Compra efetuada"
for tentativa in range(3):
    if flagcompra:
        print(info)
        break
else:
    print("Limite de tentativas efetuadas")


frutas1 = ["abacate", "banana", "morango"]
frutas2 = []

for fruta in frutas1:
    if "n" in fruta:
        frutas2.append(fruta)       #adiciona elemento na lista

print(frutas2)

#ou inline -- declara o for e a condiçao if e repete no inicio a variavel que quer acrescentar na lista
#frutas3 = [for fruta in frutas1]
#frutas3 = [for fruta in frutas1 if "n" in fruta]
#frutas3 = [fruta for fruta in frutas1 if "n" in fruta]
#assim, se esse elemento atender a condiçao ele sera incluido na lista

frutas1 = ["abacate", "banana", "morango"]
frutas3 = [fruta for fruta in frutas1 if "o" in fruta]
print(frutas3)

#lista contador
index = 0
for fruta in frutas1:
    print(index, fruta)  #(index, value)
    index +=1
#ou
for cont, fruta in enumerate(frutas1):
    print(cont, fruta)



#WHILE
'''
O loop while executa a instruçao varias vezes se a condiçao fro verdadeira
é usada quando não sabemos a quantidade de vezes que queremos executar 
'''
a =10
i = 5

while i <= a:
    print(a)
    a = a - 1

#instruçao continue
#instruçao náo seja executada em determinada contiçao ou intervalo de condiçoes, usamos continue para executar as proximas iteraçoes
a = 20
i = 4

while i <= a:
    a -= 1
    if a == 7:
        print("a was equal to 7 once")
        continue
    print(a)

#instruçao break
#instruçao náo seja executada em determinada contiçao ou intervalo de condiçoes, usamos break para parar de executar as proximas iteraçoes do loop
while i <= a:
    a -= 1
    if a == 7:
        print("a was equal to 7 once")
        break
    print(a)

#instruçao else
#se a condiçao do while náo for satisfeita, então é executado o else
i = 10

while i <= 15:
    print(i)
    i += 1
else:
    print("i is now larger than 15 that's why stopped iterating")

#exemplo while
valor = 100

while valor > 20:
    print(valor)
    valor -= 5

#exemplo while - lista
lista = [1,2,3,4,5]
tamanho = len(lista)  #len funçao que pega o tamanho
x = 0

while(x < tamanho):
    print(lista[x])
    x += 1

#inline
a = 10
i = 5
while i<= a: print(a); a -= 1

#continue e break
a = 12
i = 6
while i <= a:
    a -= 1
    if a == 7:
        print("Chegamos ao 7")
        continue
    print(a)

a = 10
i = 5
while i <= a:
    a -= 1
    if a == 7:
        print("Chegamos ao 7")
        break
    print(a)

i = 10
while i <= 15:
    print(i)
    i += 1
else:
    print("Chegamos no final do while")

#exemplo pratico
#correçao de prova onde cada questáo acertada, acrescenta 1 ponto e ao final mostra o valor total da pontuaçao
pontos = 0
questão = 1

while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "c" or resposta == "C"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "f" or resposta == "F"):
        pontos = pontos + 1
    questão += 1
print(f"O aluno teve {pontos} pontos")

