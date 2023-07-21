#variável

nome = ""
situacao = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#algoritmo 
nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a nota 1 do aluno: "))
nota2 = float(input("informe a nota 2 do aluno: "))

media = (nota1 + nota2 ) / 2

if(media >= 6 ):
    situacao = "Aprovado!"
else:
    if(media >= 4) and (media < 6):
       situacao = "Recuperação"

    else:
        situacao = "Reprovado"

print(f"{nome}, a sua média é: {media} e você está {situacao}.")
