binario = []
def contar(posicao):
    arquivo = open('day3.txt', 'r')
    zero = 0
    um = 0

    for linha in arquivo:

        linha = list(linha)
        if '\n' in linha:
            linha.remove('\n')

        if linha[posicao] == '0':
            zero+=1
        if linha[posicao] == '1':
            um+=1

    arquivo.close()
    return zero, um


for i in range(12):
    zero, um = contar(i)
    
    if zero > um:
        binario.append(0)
    else:
        binario.append(1)

print(f"gama: {binario}")
print(f"gama: 2601")

for i in range(len(binario)):

    if binario[i] == 1:
        binario[i] = 0
    elif binario[i] == 0:
        binario[i] = 1

print(f"episilon: {binario}")
print(f"episilon: 1494")

print(f"power: {2601*1494}")


