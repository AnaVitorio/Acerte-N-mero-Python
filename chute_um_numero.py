import os
import random

def cls():
    os.system('cls')

def chute_numero():
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
    jogar_nova = int(input('Você quer jogar novamente? (1)-sim / (2)-não'))
    if jogar_nova == 1:
        cls()
        chute_numero()
    elif jogar_nova == 2:
        cls()
        print("Fim")
    

chute_numero()









