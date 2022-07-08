arquivo = open('day1.txt', 'r')
lista = []
lista_soma = []
i = -2
soma = 0
aumentou = 0
for numero in arquivo:

    lista.append(int(numero))

    if i >= 0:
        soma = lista[i] + lista[i+1] + lista[i+2]
        lista_soma.append(soma)
        
    i+=1

print(lista_soma)   
for j in range(len(lista_soma)):

    if j > 0:
        if lista_soma[j] > lista_soma[j - 1]:
            aumentou +=1


print(aumentou)   
#print(lista)    
