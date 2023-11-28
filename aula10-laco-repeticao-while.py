# Exemplo 1: usando for
for c in range(1,10):
    print(c)
print('FIM')

# Exemplo 1.2: usando while
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

# Exemplo 2: usando for
for c in range(1,5):
    n = int(input('Digite um valor: '))
print('FIM')

# Exemplo 2.1: usando while
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

# Exemplo 2.2: while com função upper()
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

# Exemplo 3: while com par ou ímpar
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

# Desafio 54: leitura de sexo
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

# Desafio 55: criando um menu de opções
n1 = int(input('Primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa')
    opção = int(input('>>>>>> Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print(('Informe os números novamente: '))
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    from time import sleep
    sleep(2)
print('Fim do programa! Volte sempre!')

# Desafio 56: calculo fatorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!" = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(('{}').format(f))

# Desafio 57: sequencia de fibonacci
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')
t3 = t1 + t2
print(' -> {}'.format(t3), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('-'*30)

# Desafio 58: tratando vários valores
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um númeto [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))

# Desafio 59: maior e menor valores
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp= str(input('Quer continuar? [S/N]')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
