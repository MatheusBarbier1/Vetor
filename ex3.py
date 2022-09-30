# Vetor com os valores
a = [5, 2, 3, 8, 9]

# Vetor que guardará o resultado
b = []

# Variavel atribuida com o numero que será multiplicado pelos numeros dentro do vetor 'a'
x = int(input("Qual o multiplicador? "))

# Faz o calculo e gera o resultado que irá para o vetor 'b'
for i in range(5):
    b.append(a[i] * x)

# Escreve os resultados
print(b)
