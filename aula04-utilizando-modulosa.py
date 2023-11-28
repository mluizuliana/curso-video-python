# Exemplo 1: raiz quadrada (math.sqrt)
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}".format(num,raiz))

# Exemplo 2: raiz quadrada (math.sqrt) + arredondar para cima(math.ceil)
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}".format(num,math.ceil(raiz)))

# Exemplo 3: raiz quadrada (math.sqrt) + arredondar para baixo(math.ceil)
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {}".format(num,math.floor(raiz)))

# Exemplo 4: usando a biblioteca random (random.random número float até 1)
import random
num = random.random()
print(num)

# Exemplo 5: usando a biblioteca random (random.randint número inteiro que esteja entre A e B)
import random
num = random.randint(1,600)
print(num)

# Exemplo 6: usando biblioteca de emojis
import emoji
print(emoji.emojize("Olá mundo! :alien_monster::owl::snake:"))

# Desafio 15: retorno da parte inteira de um número real
import math
num = float(input("Digite um número real: "))
print("O número {} tem a parte inteira {}".format(num,math.floor(num)))

# Desafio 16: hipotenusa
import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print(f"O comprimento da hipotenusa é: {hipotenusa}")

# Desafio 17: angulo
import math
angulo_graus = float(input("Digite o valor do ângulo em graus: "))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f"Seno do ângulo: {seno:.2f}")
print(f"Cosseno do ângulo: {cosseno:.2f}")
print(f"Tangente do ângulo: {tangente:.2f}")

# Desafio EXTRA: quem vai botar o baseado _\|/_
import random
nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))
nome5 = str(input("Digite o quinto nome: "))
nome6 = str(input("Digite o sexto nome: "))
lista = [nome1,nome2,nome3,nome4,nome5,nome6]
escolhido = random.choice(lista)
print("O escolhido para botar um baseadao do tamanho de uma tora foi: {}".format(escolhido))

# Desafio 18: sorteio aluno
import random
nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))
lista = [nome1,nome2,nome3,nome4]
escolhido = random.choice(lista)
print("O escolhido para apagar o quadro foi: {}".format(escolhido))

# Desafio 19: ordem apresentaçao trabalho dos alunos
from random import shuffle
nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))
lista = [nome1,nome2,nome3,nome4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

# Desafio 20: abrir mp3 com módulo
exercicio abrir mp3 com módulo
import pygame
pygame.init()
pygame.mixer.music.load("C:\\Users\\meigan.uliana\\Desktop\\pythonexercicios\\Simple Plan - Perfect.mp3")
pygame.mixer.music.play()
    #reproduzir o arquivo MP3
    pygame.mixer.music.play()
    # Mantenha o programa em execução para permitir a reprodução
    while pygame.mixer.music.get_busy():
        pass  # Espera até que a música termine de tocar
    # Encerre o Pygame
    pygame.quit()
