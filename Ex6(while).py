
produto1 = 0
produto2 = 0
produto3 = 0
resposta = 1

while (resposta !=0):
    resposta = int(input("Digite o número do produto de agrado: "))
    if(resposta==1):
        produto1 = produto1 + 1
    else:
        if(resposta==2):
            produto2 = produto2 + 1
        else:
            if(resposta==3):
                produto3 = produto3 + 1

print(f"A quantidade de pessoas que gostaram do produto 1 é: {produto1}")
print(f"A quanitdade de pessoas que gostaram do produto 2 é: {produto2}")
print(f"A quantidade de pessoas que gostaram do produto 3 é: {produto3}")
    
    
