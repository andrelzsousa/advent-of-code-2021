i = 0
aumentou = 0
lista = []

arquivo = open('day1.txt', 'r')

for numero in arquivo:
    lista.append(int(numero))

    if i > 0:
        if lista[i] > lista[i - 1]:
            aumentou += 1
    i+=1

print(lista)
print(aumentou)
arquivo.close()


