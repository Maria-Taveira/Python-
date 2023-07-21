#Uma escola esta realizando matrículas para um curso aberto à
#comunidade, com limite de 20 vagas. Assumindo que os alunos são cadastrados por computador
#um algoritmo que:
# - leia a idade e o sexo do aluno
# - Informe que a turma esta lotada, quando o número de inscrtos atingir a quantidade de vagas;
# - mostre a idade média dos candidatos
# - mostre a quantidade de mulheres inscritas
# - mostre os candidatos (homens e mulheres) maiores de idade.

i = 0
idade = 0 
sexo = ""
vagas = 0
idade_media = 0.0
qntd_mulheres = 0
maior_idade = 0 
soma = 0 

for i in range (1,21,1):
    idade = int(input("Informe a idade do aluno: "))
    sexo = input("Informe o sexo do aluno: ")
    
    if(idade >= 18):
        maior_idade = maior_idade + 1

    if(sexo=="F"):
        qntd_mulheres = qntd_mulheres + 1

    soma += idade 
    media = soma / 20

if(i==2):
    print(f"Todas as vagas foram preenchidas, a sala esta lotada.")
    
print(f"A quantidade de mulheres é {qntd_mulheres}")
print(f"A quantidade de alunos maiores de idade é {maior_idade}")
print(f"A média dos alunos é {media}")