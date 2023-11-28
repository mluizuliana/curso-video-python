# Exemplo comum
cont = 1
while cont <= 10:
    print(cont, '->', end='')
    cont += 1
print('Acabou')

# Exemplo while com true: contagem de números infinitas
cont = 1
while True:
    print(cont, '->', end='')
    cont += 1
print('Acabou')

# Exemplo repetição while sem loop infinito
n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1

# Exemplo com loop infinito e break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format(s))

# Como proposta de melhoria do Python para a formatação de strings faz com que usando-se o f minúsculo antes do texto ao invés de usar .format apenas podemos adicionar a variável desejada dentro das aspas.

# Exemplos com "f strings"

# Exemplo 1
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

# Exemplo 2
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6 +
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome,idade)) # PYTHON 2

# Exemplo 3
nome = 'José'
idade = 33
salário = 987.35
printf(f'O {nome} tem {idade} anos e ganha R${salário}')

# Desafio 60: vários números com flag
n = s = 0
c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
    break
    s += n
    c += 1
print(f'Quantidade de números digitados: {c} ')
print(f'A soma vale {s}.')

# Desafio 61: tabuada
while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO')

# Desafio 62: par ou ímpar
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente?')
print(f'Game over! Você venceu {v} vezes!')

# Desafio 63: análise de dados do grupo
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = " "
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

# Desafio 64: estatísticas em produtos
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preco: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')

# Desafio 65: simulador de caixa eletrônico
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? RS'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print(('='*30))
print('Volte sempre ao BANCO CEV!')
