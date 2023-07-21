##Construir um algoritmo que leia a idade de N pessoas.
##O sistema deve calcular: a média das idades, a menor e a maior idade informada.

pessoas = 0
media = 0.0
soma = 0.0
menor = float('inf')
maior = float('-inf') 
idade = 0
i = 0

pessoas = int(input("Informe a quantidade de pessoas: "))

for i in range(1,pessoas + 1,1):
    idade = int(input("Informe a idade das pessoas: "))

    soma += idade

    if(idade < menor):   
        menor = idade
    else: 
        if(idade > maior):
            maior = idade
    

media = soma / pessoas


print(f"A média das idades é {media}.")
print(f"A maior idade é {maior}.")
print(f"A menor idade é {menor}.")

