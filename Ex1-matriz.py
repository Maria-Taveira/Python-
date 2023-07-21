#Criar um algoritmo que leia os elementos de uma matriz inteira
#5 X 5 e escreva os elemtnos da diagonal principal.

linha = 0 
coluna = 0 
matriz = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        matriz [linha][coluna] = int(input(f"Informe o número para a posição {linha+1} {coluna+1}: "))

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if(linha==coluna):
            print(f"[{matriz[linha][coluna]}]", end=' ')
    print()