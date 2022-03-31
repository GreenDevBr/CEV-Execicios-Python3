primeiro_numero = int(input("\033[39mDigite o \033[31mprimeiro\033[39m número: \033[31m"))
segundo_numero = int(input("\033[39mDigite o \033[32msegundo\033[39m número: \033[32m"))

print("\033[39m") ##RESETAR COR

if primeiro_numero > segundo_numero:
    print("O primeiro número é MAIOR")
elif primeiro_numero < segundo_numero:
    print("O segundo número é MAIOR")
else:
    print("Não existe valor maior, os dois são iguais")
