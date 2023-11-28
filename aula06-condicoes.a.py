# Exemplo 1: carro ta novo ou velho?
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print("O carro ainda é novo")
else:
    print("Ta ficando velho já")
print("--FIM--")

# Exemplo 2: modelo simplificado de if e else
tempo = int(input('Quantos anos tem seu carro?'))
print("Carro novo" if tempo <= 3 else "carro velho")
print("--FIM--")

# Exemplo 3: nome
nome = str(input("Digite seu nome: "))
if 'Meigan' in nome:
    print("Você é mó gostosão em {}!".format(nome))
else:
    print("Para você apenas bom dia {}!".format(nome))

# Exemplo 4: média
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = n1 +n2 / 2
print("A soma média foi {:.1f}".format(m))
if m >= 6.0:
    print("Parabéns a sua média foi boa")
else:
    print("Estudar mais ou será reprovado")

# Exemplo 5: média forma simplificada
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = n1 +n2 / 2
print("A soma média foi {:.1f}".format(m))
print("Parabéns" if m >= 6 else "ESTUDE MAIS!")

# Desafio 27: adivinha número
from random import randint
numero_pc = randint(1,5)
numero_usuario = int(input("Digite um número de 1 a 5:"))
if numero_pc == numero_usuario:
    print("Oba, você acertou!")
elif numero_usuario <= 0 or numero_usuario > 5:
    print("Número inválido!")
else:
    print("Você errou! :(")

# Desafio 28: multa
velocidade = float(input("Qual a velocidade que o carro estava?"))
if velocidade >= 80.0:
    print("O carro estava acima do limite permitido, a multa sera de R${}".format((velocidade - 80.0) * 7.00))
else:
    print("Não há multa para ser aplicada")

# Desafio 29: par ou impar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número {} é par!".format(numero))
else:
    print("O numero {} é impar!".format(numero))

# Desafio 30: viagem
distancia = float(input("Informe a distância da viagem(Km):"))
if distancia >= 200:
    print("O valor da passagem é: R${}".format(distancia * 0.45))
else:
    print("O valor da passagem é: R${}".format(distancia * 0.50))

# Desafio 31: ano bissexto
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

# Desafio 32: maior e menor numero
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))

# Desafio 33: aumento salario
salario = float(input("Informe seu salário: "))
if salario > 1250.00:
    print("Seu aumento é de: R${:.2f}".format((salario * 10)/100))
else:
    print("Seu aumento é de: R${:.2f}".format((salario * 15)/100))

# Desafio 34: triangulo
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))
if a + b > c and a + c > b and b + c > a:
    print("Os comprimentos podem formar um triângulo.")
else:
    print("Os comprimentos não podem formar um triângulo.")

