from time import sleep as wait
from random import randint

placar   =  [0, 0, 0]
escolhas =  ["Pedra", "Papel", "Tesoura"]
contras  =  [   3,       1,        2    ]  

for rounds in range(3):
    print(f"ROUND {rounds +1}")
    wait(0.1)
    user = int(input("[ 1 ] - Pedra\n[ 2 ] - Papel\n[ 3 ] - Tesoura\n> "))
    #computer = randint(1,3)
    computer = rounds

    print(f"O COMPUTADOR JOGOU {escolhas[computer]}, {computer}")

    if user == computer+1:
        print("EMPATE")
        placar[rounds] = 0
    elif user == contras[computer]:
        print("JOGADOR PERDE")
        placar[rounds] = -1
    else:
        print("JOGADOR GANHA")
        placar[rounds] = +1

print(f"E ESSE FOI O PLACAR: {placar}")
