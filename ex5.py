# Guarda os numeros lidos
v1 = []
# Guarda a posicao dos numeros pares
posicao_pares = []

# Guarda a soma dos pares
soma = 0

# Guarda a quantidade de numeros pares
qnt = 0


for i in range(10):
    # Lê e adiciona os 10 números na lista 'v1'
    v1.append(int(input("Qual o valor? ")))

    # Condicao para verificar se o numero lido foi par
    if v1[i] % 2 == 0:
        posicao_pares.append(i)
        soma += v1[i]
        qnt += 1

# Escreve os resultados
print("A soma dos pares é:", soma)
print("Os números pares estão nas posições:", posicao_pares)
print("A quantidade de numeros pares é:", qnt)