# Vetor que salva os nomes e notas
vet = []
 
# Adiciona o nome e a nota do aluno 
for i in range(5):
    vet.append(str(input("Digite seu nome: ")))
    vet.append(int(input("Digite sua nota: ")))

# Escreve os nomes e notas
for i in range(0, 10, 2):
    print(vet[i],":", vet[i + 1])
