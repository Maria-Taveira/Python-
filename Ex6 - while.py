##A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando 
##dados sobre o salário e número de filhos.        
##Elabore um algoritmo para apresentar:##
## a) Média do salário da população;
## b) Média do número de filhos;
## c) Maior salário;
## d) Percentual de pessoas com salário até R$ 100,00.
##O sistema deve ficar solicitando novos dados até o usuário mandar parar usando o menu:
##- Escolha uma opção:
##    1 - para cadastrar
##    2 - para sair

#duvida

i = 0
pessoas = 0
filhos = 0
media_filhos = 0.0
media_salario = 0.0
salario = 0.0
maior_salario = float("-inf")
quantidade_100 = 0
percentual_100 = 0.0
dados = 0.0


while dados != 2:
    dados = float(input("Informe a opção desejada, 1 - para cadastrar e 2 - para sair: "))

    pessoas = int(input("Informe a quantidade de pessoas: "))

    for i in range(1,pessoas,1):
         if(dados =="1"):
             for i in range(1,1+1,1): 
                  salario = float(input("Informe o salário da pessoa:R$ "))

                  if(salario <= "100"):
                        quantidade_100 += 1
                        filhos = int(input("Informe a quantidade de filho: "))
         else:
            if(dados == "2"):
                print(f"Opção sair selecionada")

         if(salario > maior_salario):
            salario = maior_salario

    media_filhos = filhos / pessoas  
    media_salario = salario/pessoas
    percentual_100 = (quantidade_100 * 100) / pessoas

    print(f"O maior salário é R${maior_salario}.")
    print(f"O percentual de pessoas com salário abaixo de R$100 é {percentual_100}%")
    print(f"A média do salário das pessoas é {media_salario}.")
    print(f"A média de filhos é de {media_filhos}.")
       

