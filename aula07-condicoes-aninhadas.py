# Exemplo 1: if, elif e else
import datetime
nome = str(input("Qual é o seu nome ?"))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil!")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal!")
print("Tenha um bom dia, {}!".format(nome))

# Desafio 35: empréstimo bancário
valor_casa = float(input("Valor da casa: "))
salario_comprador = float(input("Salário comprador: "))
anos_pagamento = int(input("Anos de parcelamento: "))
prestacao_mensal = (valor_casa / anos_pagamento) / 12
if prestacao_mensal >= (salario_comprador * 30) / 100:
    print("Não vai ser possível fazer o empréstimo, pois a parcela é maior que 30% do seu salário!")
else:
    print("O valor da mensalidade é: {:.2f}".format(prestacao_mensal))

# Desafio 36: conversao (hexadecimal, octal e hexadecimal)
num = int(input("Digite um número: "))
base_conversao = str(input("Converter para: "))
if base_conversao == "binario":
    print("{} em binário é: {}".format(num,bin(num)))
elif base_conversao == "octal":
    print("{} em octal é: {}".format(num,oct(num)))
elif base_conversao == "hexadecimal":
    print("{} em hexadecimal é: {}".format(num,hex(num)))
else:
    print("Solicitação é inválida!")

# Desafio 37: maior valor
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
if n1 > n2:
    print("O primeiro valor é maior.")
elif n2 > n1:
    print("O segundo valor é maior.")
else:
    print("Os dois valores são iguais.")

# Desafio 38: alistamento 
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
tempo_alistamento = 18 - (2023 - ano_nascimento)
if ano_nascimento < 2005:
    print("Seu tempo de alistamento já passou.")
elif ano_nascimento == 2005:
    print("Seu alistamento militar será esse ano.")
else:
    print("Ainda não está na hora de você se alistar, seu alistamento será em {} anos.".format(tempo_alistamento))

# Desafio 38.2: alistamento versao correta
from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.".format(saldo))
else:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))

# Desafio 39: média aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media > 7.0:
    print("APROVADO")
elif media < 5.0:
    print("REPROVADO")
else:
    print("RECUPERACAO")

# Desafio 40: confederação
from datetime import date
nasc = int(input("Ano nascimento: "))
idade = date.today().year - nasc
print("Sua idade é: {}".format(idade))
if idade <= 9:
    print("CATEGORIA: MIRIM")
elif idade <= 14:
    print("CATEGORIA: INFANTIL")
elif idade <= 19:
    print("CATEGORIA: JUNIOR")
elif idade == 20:
    print("CATEGORIA: SÊNIOR")
else:
    print("CATEGORIA: MASTER")

# Desafio 41: triangulo
r1 = float(input('Digite a primeira reta:'))
r2 = float(input('Digite a segunda reta:'))
r3 = float(input('Digite a terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um TRIANGULO!',  end='')
    if r1 == r2 == r3:
        print('\033[;32m  EQUILATERO!')
    if r1 != r2 != r3 != r1:
        print('\033[;32m  ESCALENO')
    if r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('\033[;32m  ISOSCELES!')
else:
    print('Não podem formar um triangulo!')

# Desafio 42: IMC
peso = float(input("PESO: "))
altura = float(input("ALTURA: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

# Desafio 43: desconto
preco_normal = float(input("Valor do produto: R$ "))
forma_pagamento = int(input("Escolha o número da forma de pagamento: \n 1: À vista no dinheiro/cheque \n 2: À vista no cartão \n 3: Em até 2x no cartão \n 4: 3x ou mais no cartão"))
if forma_pagamento == 1:
    print("O preço do produto com 10% de desconto é: R$ {}".format(preco_normal-((preco_normal*10)/100)))
elif forma_pagamento == 2:
    print("O preço do produto com 5% de desconto é: R$ {}".format(preco_normal - ((preco_normal * 5) / 100)))
elif forma_pagamento == 3:
    print("O preço do produto  é: R$ {}".format(preco_normal))
else:
    print("O preço do produto com 20% de juros é: R$ {}".format(preco_normal + ((preco_normal * 20) / 100)))


# Desafio 44: jokenpo
from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("Suas opções: \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA")
jogador = int(input("Qual é a sua jogada ?"))
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
