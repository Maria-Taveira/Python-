#variáveis
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#algoritmo 
nome = input("Informe o NOME do aluno: ")
nota1 = float(input("Informe a NOTA 1: "))
nota2 = float(input("Informe a NOTA 2: "))

media = (nota1 + nota2) / 2

print(f"{nome}, a sua média é: {media}")