#Foi feita uma pesquisa de audiência de canal de TV em várias casas
#de uma certa cidade, num determinado dia.
#3Para cada casa visitada, é fornecido o número do canal (9, 12, 23 ou 40).
#    Fazer um algoritmo que:
#       - Calcule e mostre a porcentagem de audiência de cada emissora;
#       - Caso seja digitado algum canal fora dos apresentado acima, informar como outros canais;
#       - O número 0(zero) não pode ser considerado um canal.


## dúvida



canal = 0
c9 = 0
c12 = 0
c23 = 0
c40 = 0  
porcentagem_c9 = 0
porcentagem_c12 = 0
porcentagem_c23 = 0
porcentagem_c40 = 0
i = 0
quantidade_pessoas = 0


quantidade_pessoas = int(input("Informe a quantidade de pessoas entrevistadas: "))
while canal != 0:

 for i in range(1,quantidade_pessoas+1,1):
    canal = int(input("Informe o canal assistido(9/12/23/40): "))
    if(canal == 9):
       c9 += 1
    else:
      if(canal == 12):
         c12 = c12 + 1
      else:
        if(canal == 23):
          c23 = c23 + 1
        else:
          if(canal == 40):
             c40 = c40 + 1
          else:
                print("Outro Canal")

porcentagem_c9 = (c9 * 100) / quantidade_pessoas
porcentagem_c12 = (c12 * 100) / quantidade_pessoas
porcentagem_c23 = (c23 * 100) / quantidade_pessoas
porcentagem_c40 = (c40 * 100) / quantidade_pessoas

print(f"A porcentagem do canal 9 é de : {porcentagem_c9}%")
print(f"A porcentagem do canal 12 é de : {porcentagem_c12}%")
print(f"A porcentagem do canal 23 é de : {porcentagem_c23}%")
print(f"A porcentagem do canal 40 é de : {porcentagem_c40}%")