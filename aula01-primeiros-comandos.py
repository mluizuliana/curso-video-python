# Exemplo 1: 
print('Olá, Mundo!')

# Exemplo 2: 
nome = input('Qual o seu nome ? ')
print('É um grande prazer te conhecer,', nome, '!')

# Exemplo 3:
nome = input('Qual é seu nome? ')
idade = input('Qual é sua idade? ')
peso = input('Qual é o seu peso? ')
print(nome, idade, peso) 

# Desafio 1: respondendo ao usuário
nome = input('Qual é o seu nome? ')
print('Boas vindas', nome, '!')

# Desafio 2: data nascimento
dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mes do seu nascimento? ')
ano = input('Qual o ano do seu nascimento? ')
print('A data do seu nascimento é: ', dia, '/', mes, '/', ano)

# Desafio 3: soma entre dois números
num1 = input('Informe o primeiro número a ser somado: ')
num2 = input('Informe o segundo número a ser somado: ')
  # Converta as entradas para números (assumindo que sejam números inteiros)
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print('A soma é:', soma)
