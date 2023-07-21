##Você está fazendo um trabalho de classificação de solo. Após colher uma amostra e verificar a quantidade
##de pontos de água presente nela, classificou a amostra em:
##    Rochosa: se menos ou igual a 10 pontos de água
##    Firme: se mais do 10 e menos ou igual a 40 pontos
##    Pantanosa: se mais do 40 e menos ou igual a 80 pontos
##    Quantidade Inválida: se mais do que 80 pontos


amostra = 0.0

amostra = float(input("Informe a quantidade de pontos  de água: "))

if(amostra <= 10):
    print(f"A amostra é do tipo rochosa.")
else:
    if(amostra >10 and amostra <=40):
        print(f"A amostra é do tipo firme.")
    else:
        if(amostra > 40 and amostra <=80):
            print(f"A amostra é do tipo pantanosa")
        else:
            print(f"A quantidade é inválida")


