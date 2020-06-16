import os
import random

def cls():
    os.system('cls')

numero_aleatorio = random.randint(0, 10)
#print(numero_aleatorio)
acertou = False
while not acertou:
    a = int(input("Chute um número entre 0 e 10:"))
    cls()
    if a == numero_aleatorio:
        acertou = True
        print("Parabéns!!! Você advinhou o número escolhido -- {}".format(numero_aleatorio))
    else:
        if a > numero_aleatorio:
            print("Não foi dessa vez!!")
            print("Tente um número menor")
        elif a < numero_aleatorio:
            print("Não foi dessa vez!!")
            print("Tente um número maior")

print("Fim")










