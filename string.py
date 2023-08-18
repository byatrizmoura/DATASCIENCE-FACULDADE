'''
#operaçoes basicas com string
nome = "   Python   "
frase = "Python é top"
cont = nome.count("y")   #conta os caracters selecionados
print(cont)

nova = nome.strip()   #tira os espaços
print(nova)

nova_v1 = nome.lstrip()   #tira os espaços esquerdos
print("---"+nova_v1+"---")

nova_v2 = nome.rstrip()   #tira os espaços direitos
print("---"+nova_v2+"---")

nova_v3 = frase.replace("top", "bom demais")   #substitui a palavra selecionada
print(nova_v3)

def calcular(num1, num2):
    numeros = f'O primeiro número é "{num1}" e o segundo número é "{num2}"'
    return numeros
print(calcular(1,2))

tamanho = len(frase)
print(tamanho)

#METODO DE STRING
cursos = "Python, Java, NodeJS"

curso_python = cursos [0:6]    #selecionando um trecho da lista
print(curso_python)
curso_java = cursos [8:12]
print(curso_java)
curso_select1 = cursos [8:]
print(curso_select1)
curso_select2 = cursos [:12]
print(curso_select2)

print(" "+ curso_select1 * 3)

curso_v1 = "Java"
curso_v2 = "Python"

if curso_v1 < curso_v2:
    print(f'O curso 1 de "{curso_v1}" é menor que o curso 2 de "{curso_v2}"')
else:
    print(f'O curso 1 de "{curso_v1}" é maior que o curso 2 de "{curso_v2}"')

for nome_selecionado in ["Marcelo", "Lucas", "Carlos"]:
    convite = "Olá, " + nome_selecionado + " foi convidado!"
    print(convite)

for valor in range(10):
    print(valor)

palavra_v1 = "Linguagem"
for indice in range(len(palavra_v1)):
    print(palavra_v1[indice])

#substring - Uma parte de uma string que está contida dentro de outra string
#metodo find - verifica se há uma substring
# notação de string passando início e fim de caracteres - extrair uma substring de uma string
'''
'''
atividade prática
Desenvolva um script que contemple o seguinte contexto: 
O usuário informe uma frase e o script deve identificar se a primeira palavra é “Olá”. 
Caso seja, o script deve substituir o que vem depois dessa palavra “Olá” para “pessoal”.

Um exemplo que pode ser utilizado é a frase “Olá mundo”.
'''

'''
def substituir_palavra(frase):
    palavras = frase.split()

if palavras and palavras[0] == "Olá":
    palavras[1:] = ["pessoal"]
    nova_frase = ' '.join(palavras)
    return nova_frase

# Solicitar a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Chamar a função para substituir a palavra conforme o contexto
nova_frase = substituir_palavra(frase_usuario)

# Imprimir a nova frase
print("Nova frase:", nova_frase)
'''

'''
def substituir_palavra(frase):
    palavras = frase.split()

if len(palavras) > 0 and palavras[0].lower() == "Olá" or  palavras[0].lower() == "olá":
    palavras[1:] = ["pessoal"]
    nova_frase = " " .join(palavras)
    return nova_frase
frase_usuario = input("digite aqui uma frase: ")
nova_frase = substituir_palavra(frase_usuario)
print("Nova frase: ", nova_frase)
'''


frase = input("Digite uma frase: ")
def substituir_palavra(frase):
    palavras = frase.split()
    if len(palavras) > 0 and palavras[0].lower() == "olá" or  palavras[0].lower() == "ola":
        palavras[1:] = ["pessoal"]
    nova_frase = ' '.join(palavras)
    return nova_frase

# Chamar a função para substituir a palavra conforme o contexto
nova_frase = substituir_palavra(frase)

# Imprimir a nova frase
print("Nova frase:", nova_frase)

'''
if palavras[0] == "Olá":
    palavras[1:] = ["pessoal"]

    nova_frase = ' '.join()
    print(nova_frase)


# Solicitar a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Chamar a função para substituir a palavra conforme o contexto
nova_frase = substituir_palavra(frase_usuario)

# Imprimir a nova frase
print("Nova frase:", nova_frase)
'''

def substituir_apos_ola(frase):
    palavras = frase.split()
    if len(palavras) > 0 and palavras[0].lower() == "olá" or palavras[0].lower() == "ola":
        palavras[1:] = ["pessoal"]
    nova_frase = " ".join(palavras)
    return nova_frase
frase_usuario = input("Digite uma frase: ")
nova_frase = substituir_apos_ola(frase_usuario)
print("Nova frase:", nova_frase)