import os
os.system('cls')
horizontal = 0
vertical = 0
arquivo = open('day2.txt', 'r')

for comando in arquivo:

    comando = list(comando)
    
    for i in range(len(comando)):
        key = comando[i].isdigit()
        if key == True:
            numero = comando[i]
            numero = int(numero)
   

    if comando[0] == 'f':
        horizontal+=numero
    elif comando[0] == 'u':
        vertical-=numero
    elif comando[0] == 'd':
        vertical+=numero

print(vertical*horizontal)

    
    

