## Programa feito por Green em 9/mar/2022

print("Conversor de bases numéricas")

codigo = int(input("Digite o seu código: "))
print("[ 1 ] - Para BINÁRIO \n[ 2 ] - Para OCTAL \n[ 3 ] - Para HEXADECIMAL")
user = int(input("Qual a base de conversão? "))

if user == 1:
    novo_codigo = format(codigo, "b")
    #novo_codigo = bin(codigo)
    print(f"CODIGO EM BINARIO: {novo_codigo}")
elif user == 2:
    novo_codigo = format(codigo, "o")
    print(f"CODIGO EM OCTAL: {novo_codigo}")
elif user == 3:
    novo_codigo = format(codigo, "x")
    print(f"CODIGO EM HEXADECIMAL: {novo_codigo}")
else:
    print("ERROR 001")
