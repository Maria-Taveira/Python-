'''
Faça um programa que receba o salário  base de um funcionário.
Calcule e mostre o salário a receber,sabendo que esse funcionário tem gratificação 
de R$50,00 e paga imposto de 10% sobre o salário base.
'''
salario = 0.0
salariof = 0.0

salario = float(input("Informe o salário base do funcionário: "))

salariof = salario - (salario * 0.1) + 50

print(f"O salário final do funcionário é: {salariof}")

