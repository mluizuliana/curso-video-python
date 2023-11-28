# Exemplo 1: código arcaico
num1 = input('Informe o primeiro número a ser somado: ')
num2 = input('Informe o segundo número a ser somado: ')

# Exemplo 2: convertendo as entradas para números (assumindo que sejam números inteiros)
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print('A soma é:', soma)

# Exemplo 3: código ocupando apenas uma linha
num1 = int(input('Informe o primeiro número a ser somado: '))
num2 = int(input('Informe o segundo número a ser somado: '))
soma = num1 + num2
print('A soma é:', soma)

# Exemplo 4: forma arcaida de usar o print
print('A soma é:', soma)

# Exemplo 5: forma atualizada de usar o print
print('A soma é: ()'.format(soma))

# Exemplo 6: número reconhecido como string
n1 = input('Digite seu valor: ')
print(type(n1))

# Exemplo 7: converter o número (string) em numérico (inteiro)
n1 = int(input('Digite seu valor: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
print('A soma dos valores é: ', soma)

#Exemplo 8: código mal feito, sem converter para inteiro (resultado de 5+5=55)
n1 = (input('Digite seu valor: '))
n2 = (input('Digite outro: '))
soma = n1 + n2
print('A soma dos valores é: ', soma)

# Exemplo 9: simplificando código com uso do .format
n1 = int(input('Digite seu valor: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
  #formato_velho: print('A soma de', n1, '+', n2, 'é: ', soma)
print('A soma entre {} e {} vale: {}'.format(n1,n2,soma))

# Exemplo 10: tipo primitivo float
n = float(input('Digite um valor: '))
print(n)

# Exemplo 11: tipo primitivo string 
n = str(input('Digite um valor: '))
print(type(n))

# Exemplo 12: tipo primitivo booleano 
n = bool(input('Digite um valor: '))
print(n)

# Exemplo 13: método de string .isnumeric()
n = input('Digite algo: ')
print(n.isnumeric())

# Exemplo 14: método de string .isalpha()
n = input('Digite algo: ')
print(n.isalpha())

# Exemplo 15: método de string .isalnum()
n = input('Digite algo: ')
print(n.isalnum())

# Exemplo 16: método de string .isupper()
n = input('Digite algo: ')
print(n.isupper())

# Desafio 4: soma entre dois números
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
print('A soma entre os dois valores é: {}'.format(soma))

# Desafio 5: métodos de strings
content = input('Digite algo: ')
if content.isalnum():
    print('A entrada contém apenas letras e/ou números.')
if content.isalpha():
    print('A entrada contém apenas letras do alfabeto.')
if content.isdigit():
    print('A entrada contém apenas dígitos (números).')
if content.isnumeric():
    print('A entrada é numérica (incluindo dígitos e outros caracteres numéricos, como caracteres de outros idiomas).')
if content.isdecimal():
    print('A entrada contém apenas caracteres decimais (0-9).')
if content.islower():
    print('A entrada está em letras minúsculas.')
if content.isupper():
    print('A entrada está em letras maiúsculas.')
if content.isspace():
    print('A entrada contém apenas espaços em branco.')
if content.isprintable():
    print('A entrada contém caracteres imprimíveis.')
if content.isidentifier():
    print('A entrada é um identificador válido em Python (por exemplo, uma variável válida).')
