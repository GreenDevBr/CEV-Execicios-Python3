soma = 0
multiplos = 0

for c in range(1, 501, 2):
	if c % 3 == 0:
		soma += c
		multiplos += 1

print(f"A soma de todos os ímpares no intervalo de 0 a 500 é de: {soma}\nForam {multiplos} valores multiplos de 3")