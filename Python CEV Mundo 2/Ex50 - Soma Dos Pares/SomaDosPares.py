soma = 0
contagem = 0
for c in range(1, 7):
	user = int(input(f"Digite o {c}º valor: "))
	if user % 2 == 0:
		soma += user
		contagem+=1

print(f"Você digitou 7 números e {contagem} deles, eram pares, portanto a soma é: {soma}")