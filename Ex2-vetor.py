#Criar um algoritmo que leia 10 números pelo teclado e exiba os números
#na ordem inversa da que os números foram digitados

i = 0 
vetor = [0]*10

for i in range (0,10,1):
    vetor [i] = int(input(f"Informe um número na posição {i}: "))

print(f"A seguência dos números é: ")

for i in range (9,-1,-1):
    print(f"[{vetor[i]}]", end=' ')