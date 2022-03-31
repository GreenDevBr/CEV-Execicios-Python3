peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)

print(f"Com o peso de {peso}, e a altura: {altura}, você esta: ")

if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("NO PESO IDEIAL")
elif 25 <= imc < 30:
    print("COM SOBREPESO")
elif 30 <= imc < 40:
    print("OBESO")
elif imc >= 40:
    print("EM OBESIDADE MÓRBIDA")
else:
    print("ERROR 001 - IMC INVÁLIDO")

print(f"IMC : {imc:.1f}")

