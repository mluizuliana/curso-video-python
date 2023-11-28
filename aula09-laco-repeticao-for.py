# Desafio 45: fogos artificio
from time import sleep
for cont in range(10,0,-1):
    print(cont)
    sleep(0.5)
print("BUUM ! BUUM ! POW !")

# Desafio 46: intervalo numeros pares
for cont in range(2, 51, 2):
    print(cont, end=" ")
print("FIM")

# Desafio 47: intervalo numeros impares
soma = 0
contador = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        soma = soma + cont
        contador = contador +1
print("A soma de todos os {} valores solicitados é {}".format(contador,soma))

# Desafio 48: soma valores pares
soma = 0
c = 0
for cont in range(1,7):
    num = int(input("Digite o {} valor: ".format(cont)))
    if num % 2 == 0:
        soma += num
        c += 1
print("Você informou {} números e a soma foi {}".format(cont, soma))

# Desafio 49: progressão aritmética
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo + razão,razão):
    print("{} ".format(c), end=" ➜ ")
print("ACABOU")

# Desafio 50: numeros primos
núm = int(input("Digite um número: "))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{} \n".format(c), end=" ")
print("O número {} foi divisível {} vezes".format(núm, tot))
if tot == 2:
    print("E por isso ele é PRIMO !")
else:
    print("E por isso ele não é PRIMO !")

# Desafio 51: palíndromo
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
print("O inverso de {} é {}". format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")

# Desafio 52: maioridade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input("Em que ano a {} pessoa nasceu?".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format((totmaior)))
print("E também tivemos {} pessoas menores de idade".format(totmenor))

# Desafio 53: maior e menor peso
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))
