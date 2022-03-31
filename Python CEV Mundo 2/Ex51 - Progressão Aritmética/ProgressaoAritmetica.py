primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for c in range(primeiro_termo, primeiro_termo + 9 * razao + razao, razao):
	print(f"{c} > ", end=" ")