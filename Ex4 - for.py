##Uma escola está realizando matrículas para um curso aberto à comunidade, com limite de 20 vagas.
##Assumindo que os alunos são cadastrados por computador, escreva um algoritmo que:
##- Leia a idade e o sexo do aluno;
##- Informe que a turma está lotada, quando o número de inscritos atingir a quantidade de vagas;
##- Mostre a idade média dos candidatos;
##- Mostre a quantidade de mulheres inscritas;
##- Mostre os candidatos (homens e mulheres) maiores de idade.

idade = 0
sexo = ''
media = 0.0
quantidade_mulheres = 0
quantidade_maior = 0
i = 0
soma = 0

for i in range(1,20+1,1):
    idade = int(input("Informe a idade do aluno: "))
    if(idade>=18):
        quantidade_maior += 1
    sexo = input("Informe o sexo do aluno, sendo F para feminino e M para masculino: ")
    if(sexo == "F"):
        sexo = "feminino"
        if(sexo == "feminino"):
            quantidade_mulheres += 1
    else:
        if(sexo == "M"):
            sexo = "masculino"
    if(i>21):
        print(f"A quantidade de vagas foi atingida. Sala lotada.")
    soma += idade

media = soma / 20

print(f"A média das idades dos alunos é: {media}")
print(f"A quantidade de mulheres é: {quantidade_mulheres}")
print(f"A quantidade de candidatos maiores de idade são:{quantidade_maior}")


