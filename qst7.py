import os
os.system('cls')
arquivo = open('day4.txt', 'r')

primeira = arquivo.readline().split(',')
primeira[-1] = primeira[-1].strip('\n')
print(primeira)


