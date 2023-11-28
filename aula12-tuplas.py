# Exemplo 1: variável comum
lanche = 'Hambúrguer'
lanche = 'Suco'
print('lanche') # o terminal não reconhecerá o valor "Suco" alocado na variável lanche, somente o primeiro valor "hambúrguer"

# Exemplo 2: variável com tuplas
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Exemplo 3: valores de alocação da variável
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # nesse caso o 1 é o suco pois o hamburguer é o 0

# Exemplo 4: valores negativos de alocação de variável
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-4]) # nesse caso é inverso, -4 vai ser o hamburguer, -3 o suco, -2 a pizza, -1 o pudim

# Exemplo 5: valor fatiados na alocação da variável
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3]) # será printado somente suco e pizza, pois o fatiamento desconsidera o último elemento

# Exemplo 6: valor fatiado na alocação da variável (de algum elemento até o fim)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:]) # começara no elemento 2 e irá até o fim

# Exemplo 7: valor fatiado na alocação da variável (do início, até algum elemento)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2]) # do início até o elemento 2, lembrando que o fatiamento desconsidera o último elemento

# Exemplo 8: valor fatiado na alocação da variável (com valores negativos)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])

# Exemplo 9: tuplas combinadas com for
    # No código, comida é utilizada como uma variável temporária dentro do loop for. Na primeira iteração do loop, comida recebe o valor do primeiro elemento da tupla lanche, na segunda iteração recebe o segundo elemento e assim por diante, até percorrer todos os elementos da tupla.
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# Exemplo 9.1:
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

# Exemplo 9.2: tuplas combinadas com len (largura)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

# Exemplo 9.3: tuplas combinadas com len (largura)
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

# Exemplo 9.4: tuplas com print e sorted
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)

# Exemplo 10: print da soma de duas tuplas
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)

# Exemplo 11: print da soma de duas tuplas + count
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c.count(5))

# Exemplo 12: print da soma de duas tuplas + index
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c.index(8)) # index retorna a posição de 8

# Exemplo 12.1: print da soma de duas tuplas + (index de números iguais)
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c.index(5,1)) # index retorna a posição de 8, quando há valores iguais, usar a vírgula para indicar a ordem da ocorrência

# Exemplo 13: deletando tupla
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # quando executado irá retornar um erro, 'pessoa' is not defined, pois apagará tudo da memória, inclusive a variável
print(pessoa)

# Desafio 66: número por extenso
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[núm]}')

# Desafio 67: tuplas com times de futebol
times = ('Corintians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo','Atletico-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória','Coritiba','Avaí','Ponte Preta','Atlético-GO')
print('-=' *40)
print(f'Lista de times do Brasileirão: {times}')
print('-=' *40)
print(f'OS 5 primeiros times são: {times[0:5]}')
print('-=' *40)
print(f'OS 4 últimos times são: {times[-4:]}')
print('-=' *40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' *40)
print(f'O Chapecoense esta em {times.index("Chapecoense")+1}ª posição')

# Desafio 68: maior e menor valores em tupla
from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

# Desafio 69: análise de dados um uma tupla
núm = (int(input('Digite um número:')),
        int(input('Digite outro número:')),
        int(input('Digite mais um número:')),
        int(input('Digite o último número:')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apoareceu {núm.count(9) vezes}')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores parem digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end= '')

# Desafio 70: lista de preços com tupla
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' *40)
print(f'{"LISTAGEM DE PREÇOS:^40"}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else: print(f'RS{listagem[pos]:>7.2f}')
print('-' * 40)

# Desafio 71: contando vogais em tupla
palavras = ('aprender', 'programa', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('letra', end='')
