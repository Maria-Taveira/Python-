'''
Você está fazendo um trabalho de classificação de solo. Após colher uma amostra e verificar 
a quantidade de pontos de água presente nela, classificou a amostra em:
        ROCHOSA: se menos ou igual a 10 pontos de água.
        FIRME: se mais de 10 e menos  ou igual a 40 pontos.
        PANTANOSA: se mais de 40 e menos ou igual a 80 pontos.
        QUANTIDADE INVÁLIDA: se mais do que 80 pontos.
'''
amostra = 0.0

amostra = float(input("Informe a quantidade de pontos de água presente na amostra: "))
if(amostra <= 10):
    amostra = input("A mostra é do tipo ROCHOSA.")
else:
    if(amostra >10 and amostra <=40):
        amostra = input("A amostra é do tipo FIRME.")
    else:
        if(amostra>40 and amostra <=80):
            amostra = input("A amostra é do tipo PANTANOSA.")
        else:
            amostra = input("Quantidade Inválida.")
