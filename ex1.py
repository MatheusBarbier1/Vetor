# Os 2 vetores
v1 = []
v2 = []

# Lista para guardar o resultado
resultados = []

# Pega os valores e da os resultados
for i in range(3):
    v1.append(int(input("Qual a força1? ")))
    v2.append(int(input("Qual a força2? ")))
    resultados.append(v1[i] + v2[i])

# Escreve o resultado  
print(resultados)