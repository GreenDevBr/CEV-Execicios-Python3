nota01 = float(input("Digite a sua primeira nota: "))
nota02 = float(input("Digite a sua segunda nota: "))

media = (nota01+nota02)/2
print(f"Com a média {media} você foi: ")

if media < 5:
    print("REPROVADO")

elif 5 >= media < 7:
    print("RECUPERAÇÃO")

elif 7.0 <= media <= 10:
    print("APROVADO")

else:
    print("Error 001 - nota incorreta")
