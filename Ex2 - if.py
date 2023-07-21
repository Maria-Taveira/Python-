##Construa um algoritmo que determine quanto será gasto para encher o tanque de um carro.
## O usuário fornecerá os seguintes dados: Tipo de carro (TC) (G – gasolina ou A – álcool)
## e Capacidade do tanque (CT), em litros. Após a escolha do tipo de veículo 
##e da capacidade do tanque, o sistema irá imprimir uma mensagem falando o tipo 
##do carro(Gasolina ou álcool) e pedirá para o usuário informar o valor do preço do litro do combustível.
##Como saída, será informado para o usuário, o valor, em reais, do preço de se encher tanque de combustível.

gasto = 0.0
tipo_carro = ""
capacidade_tanq = 0.0
preço = 0.0

tipo_carro = input("Informe o tipo do carro, G para gasolina ou A para álcool: ")
if(tipo_carro == "G"):
    tipo_carro = "Gasolina"
else:
    if(tipo_carro == "A"):
        tipo_carro = "Álcool"
    else:
        print(f"Tipo de carro desconhecido")

capacidade_tanq = float(input("Informe a capacidade do tanque em litros: "))

print(f"O carro é do tipo {tipo_carro} e sua capacidade é de {capacidade_tanq} litros.")

preço = float(input("informe o preço do combustível: "))

gasto = preço * capacidade_tanq

print(f"O tanque cheio do automóvel custará R${gasto}.")
