import os
os.system('cls')
horizontal = 0
vertical = 0
aim = 0
arquivo = open('day2.txt', 'r')

for comando in arquivo:
   
    for i in range(len(comando)):
        key = comando[i].isdigit()
        if key == True:
            numero = comando[i]
            numero = int(numero)
 
    
    if comando[0] == 'f':
        horizontal+=numero
        vertical+=numero*aim
    elif comando[0] == 'u':
        aim-=numero
    elif comando[0] == 'd':
        aim+=numero

print(vertical*horizontal)


    
    

