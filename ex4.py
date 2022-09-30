import random

# Vetor que guarda os numeros de 1 a 6
v1 = []

# Guarda a quantidade de vezes que caiu o numero 1 a 6
ocorrencias = [0, 0, 0, 0, 0, 0]

# Guarda a porcentagem que caiu cada numero
porcentagens = [0, 0, 0, 0, 0, 0]

# Faz os 50 numeros e guarda quantas vezes caiu de 1 a 6
for i in range(50):
    v1.append(random.randrange(1, 7))
    match(v1[i]):
        case 1: 
            ocorrencias[0] += 1
        case 2: 
            ocorrencias[1] += 1
        case 3: 
            ocorrencias[2] += 1
        case 4: 
            ocorrencias[3] += 1
        case 5: 
            ocorrencias[4] += 1
        case 6: 
            ocorrencias[5] += 1

# Faz a porcentagem de cada numero (1 a 6)
for i in range(6):
    porcentagens[i] = (ocorrencias[i] / len(v1)) * 100

# Escreve os resultados
print("O numero 1 apareceu {:0.2f}% das vezes, o numero 2 apareceu {:0.2f}% das vezes".format(porcentagens[0], porcentagens[1]))
print("O numero 3 apareceu {:0.2f}% das vezes, o numero 4 apareceu {:0.2f}% das vezes".format(porcentagens[2], porcentagens[3]))
print("O numero 5 apareceu {:0.2f}% das vezes, o numero 6 apareceu {:0.2f}% das vezes".format(porcentagens[4], porcentagens[5]))