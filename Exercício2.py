'''
O custo ao consumidor d um carro novo é a soma do preço de 
fábrica com percentual de lucro do distribuidor e dos impostos ao preço 
de fábrica. FAça um programa que receba o preço de fábrica de um veículo, o percentual 
de lucro do distribuidor e o percentual de impostos.
calcule e mostre:
        a) o valor correspondente ao lucro do distribuidor;
        b) o valor correspondente ao imposto;
        c) o preço final de veículo
'''

preco_fabrica = 0.0
lucro_distribuidor = 0.0
impostos = 0.0
custo_consumidor = 0.0

preco_fabrica = float(input("Informe o preço de fábrica de um veículo: "))
lucro_distribuidor = float(input("Informe o percentual de lucro do distribuidor: "))
impostos = float(input("Informe o percentual de impostos a serem cobrados: "))


custo_consumidor = preco_fabrica + (preco_fabrica * (lucro_distribuidor/100)) + (preco_fabrica * (impostos/100))  

print(f"O lucro do distribuidor é: R$ {preco_fabrica * (lucro_distribuidor/100):,.2f}")
print(f"O valor do imposto é: R$ {preco_fabrica * (impostos/100):,.2f}")
print(f"O valor a ser pago pelo consumidor é: R$ {custo_consumidor:,.2f}")
