#Construir um algoritmo que leia a idade de N pessoas
#O sistema deve calcular: a média das idades, a menor idade e a maior idade informada

i = 0 
idade = 0 
media = 0.0
soma = 0
menor = 0 
maior = 0 
qntd_pessoas = 0

qntd_pessoas = int(input("Informe a quantidade de pessoas: "))

for i in range(1,qntd_pessoas,1):
    idade = int(input("Informe a idade: "))

    soma = soma + idade
    media = soma / i


    if (i==1):
        menor = idade
        maior = idade
    else:
        if(idade > maior):
            maior = idade
        else:
            if(idade < menor):
               menor = idade

print(f"A maior idade é de {maior}.")
print(f"A menor idade é de {menor}.")
print(f"A média das idades é {media}.")