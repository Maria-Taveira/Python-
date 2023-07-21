#variável

i = 0 
numero = 0 

#algoritmo 
numero = int(input("Informe o número para a tabuada: "))


for i in range(1,11,1):
    print(f"{numero} X {i} = {numero * i}") 
    