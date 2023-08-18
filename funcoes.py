'''
FUNÇÕES
Toda vez que for realizar uma tarefa especifica, as funções ajudam a tornar o codigo menor e mais flexivel,
podendo ser reutilizado varias vezes.
ex.: print()
'''
# /n pula uma linha
#exemplo
def add_number(x,y):
    sum = x + y
    return sum

num1 = 5
num2 = 6

print("The sum is", add_number(num1,num2))

#exemplo
def boas_vinda(nome,idade):
    print(f"Olá {nome}, você tem {str(idade)} anos de idade!")
boas_vinda("Marcelo", 33)


#exemplo - Cadastrar pessoas
def cadastrar(pessoas):
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu NOME: ")
    idade = int(input("Digite seu IDADE: "))
    pessoas.append((cpf,nome,idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f"Nome {nome}, possui {idade} anos de idade e é portador(a) do CPF {cpf}")

def exibir_menu():
    print(''' \n Escolha uma opção:
    1. Cadastrar pessoa
    2. Listar pessoa
    3. Sair''')

def main():
    pessoas = []
    flag = True
    while flag:  #se a tag for verdadeira
        exibir_menu()
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
                print("Operação finalizada!")
            else:
                print("Opção inválida!")
        except ValueError:
            print("Favor digitar somente números")
main()

# CONHECENDO COLEÇOES
# Trabalhando com iterações dentro de coleções
'''
Funçao map() - é uma funçao integrada no pyhton que permite aplicar uma funçao para cada item iterável
(como uma lista ou um dicionario) e retorna um novo iterador que pode ser usado em outras partes do codigo.
map(function, iteravel,[iteravel2, iteravel3,...])
'''

def calculateSquare(n):
    return n*n

numbers = (1,2,3,4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set (conjunto)
numbersSquare = set(result)
print(numbersSquare)

'''
Funçao lambda()
É semelhante a funçao map, mas para expressões menos complexas, pois a lambda fica somente em uma linha de codigo.
Basicamente, seria escrever a funçao na mesma linha do map ao inves de defini-la antes.
map(lambda item: item[] expression, iteravel)
'''
#map com uma funçao lambda
numbers = [10,15,21,33,42,55]
mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
print(mapped_numbers)

'''
Funçao filter()
filtra com base nos parametros
filter(function, iteravel)
é aplicado em cada elemento do itevável e se retornar True, o elemento é selecionado por essa funcao filter
'''
def verifica(numero):
    if numero % 2 == 0:  #resto da divisão por 2 é igual a 0
        return True
    return False

numeros = [1,2,3,4,5,6,7,8,9,10]

#Se um elemento passado para verifica() retorna True, selecione-o
numeros_selecionados = filter(verifica, numeros)

#converte em lista
lista_numeros = list(numeros_selecionados)

print(lista_numeros)

#exemplo
lista1 = [1,2,3,4]

def multiplicacao(x):
    return x * 2

lista2 = map(multiplicacao, lista1)  #aqui ele converte para objeto

print(list(lista2))  #aqui ele retorna o resultado da funçao e converte para uma lista

#exemplo - map com lambda
lista3 = list(map(lambda x: x * 2, lista1)) #aplica a funçao na mesma linha do map e já converte para uma lista

print(lista3)

#exemplo
usuarios = [("contato@gmail.com", True),("adm@gmail.com", True),("secretaria@gmail.com", False)]
def getEmail(usuario):
    return usuario[0]

def valido(usuario):
    return usuario[1] == True

print(list(map(getEmail,usuarios)))
print(list(filter(valido,usuarios)))

emails = list(map(getEmail, filter(valido, usuarios)))
print(emails)

'''
Criando nosso próprio módulo

Além de importar módulos internos, também podemos criar nossos próprios módulos. Isso é muito útil se você tiver algumas funções que deseja reutilizar em outros projetos. Criar um módulo é simples. Basta salvar o arquivo com a extensão .py e colocá-lo na mesma pasta do arquivo Python do qual você o importará. Suponha que você queira usar a função verificarNumeroPrimo() definida anteriormente. Veja como fazer isso: Primeiro, salve o código como codigo.py na sua área de trabalho. codigo.py deve ter o seguinte código:

def verificarNumeroPrimo(y):

for x in range(2, y):

if (y % x == 0):

return False

return True

Em seguida, crie outro arquivo Python e nomeie-o como usarModulo.py. Salve-o também na sua área de trabalho. usarModulo.py deve ter o seguinte código.

import codigo

resposta = codigo.verificarNumeroPrimo(16)

print(resposta)

Agora execute usarModulo.py. Você deve obter a saída True. Simples assim.

No entanto, suponha que você queira armazenar codigo.py e usarModulo.py em pastas diferentes. Você terá que adicionar alguns códigos para usar o módulo verificarNumeroPrimo.py, informando ao interpretador Python onde encontrar o módulo.

Digamos que você criou uma pasta chamada ‘modulos’ no seu disco C e salvou codigo.py nela. Você precisa adicionar o seguinte código no topo do seu arquivo usarModulo.py (antes da linha import codigo).

import sys

if ‘C:\modulos’ not in sys.path:

sys.path.append(‘C:\modulos’)

sys.path se refere ao caminho do sistema do seu Python. Esta é a lista de diretórios que o Python percorre para procurar módulos e arquivos. O código acima anexa a pasta ‘C:\modulos’ ao caminho do sistema.

Agora você pode colocar codigo.py em ‘C:\modulos’ e usarModulo.py em qualquer outra pasta de sua escolha.


'''


# PESQUISAR SOBRE NAMESPACE
