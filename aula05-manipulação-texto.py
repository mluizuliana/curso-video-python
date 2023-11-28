#fatiamento de string
frase = "Curso em vídeo Python"
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2]) #último número significia pular de dois em dois
print(frase[:5]) #somente até o 5 (porém cinco não retorna)
print(frase[15:]) #fatia do 15 até o final da string
print(frase[9::3]) #começa no nove e vai até o final da string

#analise de string
frase = "Curso em vídeo Python"
print(len(frase)) #comprimento da frase
print(frase.count('o')) #conta quantos caracteres (nesse caso 'o') tem na frase
print(frase.count('o',0,13)) #conta quantos caracteres (nesse caso 'o') tem na frase do caractere 1 até o 13
print(frase.find('deo')) #filtra apenas pela sequencia de caracteres 'deo'
print(frase.find('Android')) #retorna -1 caso não exista a busca 'Android'
print('Curso' in frase) #retorna true or false se houver / se não houver curso no contexto

#transformação de string
frase = "Curso em vídeo Python"
print(frase.replace('Python','Android')) #substitui o primeiro termo pelo segundo
print(frase.upper()) #tudo maiúsculo
print(frase.lower()) #tudo minúsculo
print(frase.capitalize()) #apenas a primeira de todas as letras maiúscula
print(frase.title()) #todos os primeiros caracteres maiúsculas
frase_strip = "   Aprenda Python   "
print(frase_strip.strip()) #remover espaços inúteis antes ou depois dos caracteres

#junção e divisão de string
frase = "Curso em vídeo Python"
divisao = frase.split() #divisão dentro da string baseada em cada espaço
print(divisao)
juncao = '-'.join(divisao) #juncao dentro da string baseada em cada espaço
print(juncao)

# Desafio 21: analisador de textos
nome = str(input("Digite seu nome completo: "))
print(nome.upper()) #TODAS AS LETRAS SE TORNAM MAIUSCULAS
print(nome.lower()) #TODAS AS LETRAS SE TORNAM MINUSCULAS
espacosvazios = nome.count(' ') #CONTEI TODOS OS ESPAÇOS VAZIOS NA STRING E ARMAZENEI
espacototal = len(nome) #CONTEI TODOS OS ESPAÇOS DA STRING SEM EXCESSÃO
print('Total de letras: {}'.format(espacototal - espacosvazios)) #PRINTEI O ESAÇO TOTAL -  OS VAZIOS.
nome1 = nome.split() #DIVIDÍ A STRING EM STRINGS MENORES COM SPLIT
print('Total de letras do primiro nome: {}'.format(len(nome1[0]))) #PRINTEI O NUMERO DE LETRAS DA PRIMEIRA STRING DO SPLIT

# Desafio 22: separando dígitos de um número
numero = int(input("Digite um número de 0 a 9999: "))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10
print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

# Desafio 23: verificando as primeiras letras de uma frase 
nome = str(input("Digite o nome de sua cidade: "))
santo = "Santo" in nome
    if santo == True:
        print("A cidade recebe o nome Santo .")
    else:
        print("A cidade não possui Santo no nome.")

# Desafio 24: procurando uma string dentro de outra
nome = str(input("Digite o seu nome: "))
silva = "Silva" in nome
    if silva == True:
        print("Seu nome tem Silva.")
    else:
        print("Seu nome não tem Silva.")

# Desafio 25: primeira e última ocorrência dentro de uma string 
frase = str(input("Digite qualquer frase: "))
print(frase.count('A'))
letra = 'A'
count = frase.count(letra)
primeira_posicao = frase.find(letra)
ultima_posicao = frase.rfind(letra)
print("Quantidade de letras A: {}".format(count))
print("Primeira aparicao: {}".format(primeira_posicao))
print("Ultima aparicao: {}".format(ultima_posicao))

# Desafio 26: primeiro e último nome de uma pessoa
nome = str(input("Digite seu nome completo: "))
nome_separado = nome.split()
print("Nome completo: {}".format(nome))
print("Primeiro nome: {}".format(nome_separado[0]))
print("Último nome: {}".format(nome_separado[-1]))
