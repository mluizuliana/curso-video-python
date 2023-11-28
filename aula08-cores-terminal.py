# Texto colorido
print("\033[31mTexto vermelho\033[m")
print("\033[32mTexto verde\033[m")
print("\033[33mTexto amarelo\033[m")
print("\033[34mTexto azul\033[m")
print("\033[35mTexto roxo\033[m")
print("\033[36mTexto ciano\033[m")

# Texto em negrito
print("\033[1mTexto em negrito\033[m")

# Texto sublinhado
print("\033[4mTexto sublinhado\033[m")

# Combinação de formatação
print("\033[1;31;4mTexto em negrito, vermelho e sublinhado\033[m")

# Fundo colorido
print("\033[41mFundo vermelho\033[m")
print("\033[42mFundo verde\033[m")
print("\033[43mFundo amarelo\033[m")
print("\033[44mFundo azul\033[m")
print("\033[45mFundo roxo\033[m")
print("\033[46mFundo ciano\033[m")

# Combinando texto colorido com fundo colorido
print("\033[31;42mTexto vermelho com fundo verde\033[m")

# Outros exemplos
print("\033[1;33;41mTexto em negrito, amarelo com fundo vermelho\033[m")
print("\033[36;44mTexto ciano com fundo azul\033[m")
