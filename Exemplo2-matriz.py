#variáveis 
linha = 0 
coluna = 0 
matriz = [[0.0]*3,[0.0]*3,[0.0]*3]

#algoritmo 
for linha in range (0,3,1):
    for coluna in range(0,3,1):
        matriz[linha][coluna] = float(input(f"Informe o número para a posição {linha} {coluna}: "))

for linha in range (0,3,1):
    for coluna in range (0,3,1):
        print(f"[{matriz[linha][coluna]}]", end=' ')
    print()
