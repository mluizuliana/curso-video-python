# Exemplo 1: multiplicação
print('='*20)

# Exemplo 2: alinhamento
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=<20}!'.format(nome))
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=>20}!'.format(nome))

# Exemplo 3: operação dentro do .format
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor '))
print('A soma vale {}'.format(n1+n2))

# Exemplo 4: fazendo a operação dentro da variável
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {} '.format(s,m,d))
print('Divisão inteira é {} e a potencia é {}'.format(di, e))

# Exemplo 5: formatando a saida do valor no terminal, uso do end para nao quebrar a linha e /n para quebrar a linha
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\no produto é {}, e a\ndivisão é {:.3f}'.format(s,m,d)) # {:.3f} usada dentro de uma string de formatação para controlar a formatação de números de ponto flutuante (floats), onde dois pontos é usado para iniciar uma especificação de formatação 
print('Divisão inteira é {} e a potencia é {}'.format(di, e))

# Exemplo 6: end=' ' para nao quebrar a linha
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},o produto é {}, e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira é {} e a potencia é {}'.format(di, e))

# Exemplo 7: /n para quebrar a linha
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, \n e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira é {} e a potencia é {}'.format(di, e))

# Desafio 6: antecessor e sucessor
n1 = int(input('Digite um valor: '))
print('O número antecessor de {} é {}, e o sucessor é {}.'.format(n1,n1-1,n1+1))

# Desafio 7: dobro, triplo e raiz quadrada
n1 = int(input('Digite um valor: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(n1,n1*2,n1*3,n1**0.5))

# Desafio 8: nota média aluno
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
print('A média do aluno é: {}'.format((n1+n2)/2))

# Desafio 9: pintar parede
largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura*altura
qtd_litros = area/2
print('A área da parede é {} e a quantidade de litros necessário para pintar a parede é {}'.format(area, qtd_litros))

# Desafio 10: salario aumento 15%
salario = float(input('Informe o salário do funcionário: '))
print('O salário com 15% de aumento é R$ {:.2f}'.format(salario+(salario*15)/100))

# Desafio 11: conversor de medidas
valor_metros = float(input('Informe o valor em metros: '))
print("{:.2f} em cm é {:.2f} e em milimetros é {:.2f}".format(valor_metros, valor_metros*100, valor_metros*1000))

# Desafio 12: tabuada
n1 = int(input('Digite um número: '))
print('A tabuada de {} é: \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(n1,n1,n1*1,n1,n1*2,n1,n1*3,n1,n1*4,n1,n1*5,n1,n1*6,n1,n1*7,n1,n1*8,n1,n1*9,n1,n1*10))

# Desafio 13: conversor de moedas
real = float(input("Quanto dinheiro você tem na carteira? "))
dolar = real / 3.27
print('Com {:.2f} reais você pode comprar {:.2f} dólares'.format(real,dolar))

# Desafio 14: desconto
preco = float(input("Informe o valor do produto: "))
desconto = (preco * 5)/100
print("O valor do produto com 5% de desconto é {}".format(preco-desconto))













