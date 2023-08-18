'''
OPERADORES DE IDENTIDADE
is -- mostra True se ambos operadores forem identicos
ex.: a = 20   b=20  print(a is b) // True
is not -- mostra True se os operadores não forem identicos
ex.: d = 20  e = 21  print(d is not e) // True

--

OPERADORES DE ASSOCIAÇÃO
in -- se o valorque esta procurando na sequencia existir ele retorna True
not in - retorna True se o valor procurado não existe na sequencia
'''

#exercicio
#como eu fiz
num1 = int(input("Qual seu salario mensal? "))
num2 = int(input("Qual % de reajuste? "))
resultado = num1 + (num1*(num2/100))
print("O salario com o reajuste é: ", resultado)

#como o professor fez
salario = int(input("Qual o salario mensal? "))
reajuste = int(input("Qual o reajuste? "))
aumento = salario * reajuste/100
salarioFinal = salario + aumento
print("O salario reajustado é: ", salarioFinal)

#exercicio pratico2
'''
Atividade Prática 2 - Variáveis e tipos de dados

Título da Prática: Aplicar os conceitos de operadores

Objetivos: Calcular o custo final de um carro ao consumidor

Materiais, Métodos e Ferramentas: Para realizar esta prática vamos utilizar o PyCharm

Atividade Prática
Desenvolva um programa que contemple o seguinte contexto: 
O custo de um carro novo para o consumidor é a soma do custo de fábrica 
com a porcentagem do distribuidor e os impostos (aplicados ao custo de fábrica). 
Supondo que o percentual do distribuidor seja de 28% e os impostos sejam de 45%, 
escreva um código no qual o usuário deve informar o custo de fábrica de um carro e, 
em seguida, calcular e apresentar no console o custo final para o consumidor.
Onde:
Custo de fábrica é o valor base do carro.
Percentual do distribuidor é a porcentagem do custo de fábrica que o distribuidor adiciona ao valor do carro.
Impostos é a porcentagem do custo de fábrica que é aplicada como impostos sobre o valor do carro.
Utilizando os valores fornecidos (percentual do distribuidor de 28% e impostos de 45%), a fórmula fica assim:
Custo final = Custo de fábrica + (Custo de fábrica * 0.28) + (Custo de fábrica * 0.45)
'''

cFab = int(input("Informe o valor do custo de fábrica do carro: "))
cfCar = cFab + (cFab * 0.28) + (cFab * 0.45)
print(cfCar)