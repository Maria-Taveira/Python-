#variável
numero = 0 

#algoritmo 
while numero != 1:
    print(f"O valor da variável número é: {numero}")
    numero = int(input("Informe 1 - Para parar ou qualquer número para coninuar: "))
    if(numero == 1):
        print(f"Procedimento finalizado.")