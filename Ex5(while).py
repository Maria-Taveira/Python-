#faça um algoritmo que solicite N números inteiros até que o 
#número 0 seja digitado. Ao final o algoritmo deve informar o maior e o 
#menor número digitado.
#OBS: O número 0 não pode ser contado.

numero = 0 
maior = 0
menor = 0


numero = int(input("Informe um número: "))
maior = numero 
menor = numero 

while (numero != 0):
    if(numero > maior):
        maior = numero 
    
    if(numero < menor) and (numero != 0):
        menor = numero


    numero = int(input("Informe um número: "))
    
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
