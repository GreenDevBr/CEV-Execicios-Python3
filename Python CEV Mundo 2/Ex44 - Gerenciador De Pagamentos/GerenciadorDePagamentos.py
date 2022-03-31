compras = float(input("Preço das compras: R$: "))

print('''FORMAS DE PAGAMENTO
[ 1 ] - À vista   ( dinheiro/cheque )
[ 2 ] - À vista   ( cartão )
[ 3 ] - Parcelado ( cartão )''')

user = int(input("Qual a opção? "))

if user == 1:
    calc = compras - (compras * (10/100))

elif user == 2:
    calc = compras - (compras * (5/100))

elif user == 3:
    parcelas = int(input("Quantas parcelas? "))
    if 0 < parcelas <= 2:
        calc = compras
    elif parcelas >= 3:
        calc = compras + (compras * (20/100))
    print(f"Parcelando de {parcelas} vezes de {calc / parcelas}")
else:
    calc = 0
    compras = 0
    print("ERROR OPÇÂO INVÁLIDA")

print(f"De {compras:.2f} R$, agora vai custar: {calc:.2f} R$")
