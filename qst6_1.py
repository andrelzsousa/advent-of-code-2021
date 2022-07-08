import os
os.system('cls')

def verifica(posicao):
    zero = 0
    um = 0
    lis_1 = []
    lis_0 = []
    lista = []

    arquivo = open('day3s.txt', 'r')
    for linha in arquivo:
        lista.append(linha.strip('\n'))   
    arquivo.close()
    print(lista)


    arquivo = open('day3s.txt', 'r')
    for numero in arquivo:

        numero = numero.strip('\n')
        lis_numero = list(numero)
   
        if lis_numero[posicao] == '1':
            um+=1
            lis_1.append(numero)
            
        elif lis_numero[posicao] == '0':
            zero += 1
            lis_0.append(numero)

    arquivo.close()

    arquivo = open('day3s.txt', 'w')
    if um < zero:
        for num in lis_1:
            arquivo.write(num + '\n')

    elif um > zero:
        for num in lis_0:
            arquivo.write(num + '\n')
    
    elif um == zero:
        for num in lis_0:
            arquivo.write(num + '\n')
        
    arquivo.close()




for i in range(9):
    verifica(i)