#Faça um algoritmo que leia 30 números reais em um vetor e depois mostre os números
#localizados nas posições ímpares.

i = 0 
vetor = [0.0]*30

for i in range(0,30,1):
     vetor[i] = float(input(f"Informe o número da posição {i}: "))

for i in range(0,30,1):
    if(i%2 != 0):
        print(f"[{vetor[i]}]", end='')