import os
import random

def cls():
    os.system('cls')

def chute_numero():
    numero_aleatorio = random.randint(0, 10)
    print('-------VOCÊ TEM 3 CHANCES DE ACERTAR O NÚMERO SORTEADO------------')

    for tentativa in range(1, 4):
        a = int(input("Chute um número entre 0 e 10:"))
        cls()
        if a > numero_aleatorio:
            print("Tente um número menor")
        elif a < numero_aleatorio:
            print("Tente um número maior")
        else:
            break

    if a == numero_aleatorio:
        cls()
        print("Parabéns!!! Você advinhou o número escolhido --> {}".format(numero_aleatorio))
    else:
        cls()
        print('FIM DE JOGO - não foi dessa vez, o número sorteado foi --> {}'.format(numero_aleatorio))

    jogar_nova = int(input('Você quer jogar novamente? (1)-sim / (2)-não'))
    if jogar_nova == 1:
        cls()
        chute_numero()
    elif jogar_nova == 2:
        cls()
        print("Tchau")


chute_numero()









