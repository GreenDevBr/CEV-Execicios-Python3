valor = int(input("Digite o valor para ver os seus multiplos: "))
fim = int(input("Quantas multiplicações?\n"))
resultado = f"Tabuada de {valor}"

for c in range(1, fim+1):
	resultado = f"{resultado}\n{valor} x {c} = {valor * c}"

print(resultado)