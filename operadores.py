"""
**Operadores de associaçao

**Operadores de atribuiçao

**Operadores relacionais ou de comparaçao

**operadores aritmeticos
realizam operaçoes matematicas

"""

#operadores aritmeticos

a = 20
b = 15
print (a + b) #adiçao
print (a - b) #subtraçao
print (a / b) #divisao
print (a * b) #multiplicaçao
print (a ** b) #expoente -- o valor do lado direito se torna expoente do esquerdo
print (a % b) #modulo -- retorna o restante da divisao
print (a // b) #divisao do andar -- divide o valor do esquerdo pelo direito e retorna o menor e o inteiro mais proximo sendo assim a saida sempre sera um inteiro e nunca um float


#operadores logicos
'''
uteis codigos em que há testes
and, or, not
print(x and s) -- toda vez que x ou s for falso, z (resultado) sera falso
print(x or s) -- toda vez que x ou s for verdadeiro, z (resultado) sera verdadeiro
print(not x) -- será contrario, por exemplo, se x for verdadeiro então not x é falso
'''
x = False
y = True
print(x and y)
print(x or y)
print(not x )

'''
PRIORIDADES
- OPERADORES ARITMETICOS
1 PARENTESES
2 MULTI, DIV, MODULO
3 SOMA E SUBTRAÇAO

-OPERADORES RELACIONAIS
1 PARENTESES
2 MAIOR/MAIOR OU IGUAL/MENOR/MENOR OU  IGUAL
3 IGUAL/DIFERENTE

- OPERADORES LOGICOS
1 PARENTESES
2 NOT (NAO)
3 AND (E)
4 OR (OU)
'''

#EXEMPLO
a = 25 + 1 > 25 -1 and 2 * 10 + 5 == 24 + 1
print(a)
'''
a = 26 > 24 and 25 == 25
a = true and true
a = true
'''
# exercicio: faça um algoritmo que leia 2 numeros inseridos pelo usuário, depois verifique se o primeiro é maior que o segundo
x = int(input("insira um número para x: "))
y = int(input("insira um número para y: "))
'''
resultado = x > y
print(resultado)
ou
'''
if x > y:
    print("O primeiro número é maior que o segundo número")


#Operadores de distribuição
x = 10
y = 20

print(x == y) #false igual
print(x != y) #true  diferente
print(x > y) #false maior
print(x < y) #true  menor
print(x >= y) #false menor igual
print(x <= y) #true maior igual

