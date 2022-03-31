import datetime

ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = datetime.date.today().year - ano_de_nascimento

print(f"Você tem {idade} anos, então você é:")

if idade <= 9:
    print("MIRIM")

elif 9 < idade <= 14:
    print("INFANTIL")

elif 14 < idade <= 19:
    print("JUNIOR")

elif 19 < idade <= 25:
    print("SÊNIOR")

elif 25 < idade <= 110:
    print("MASTER")

else:
    print(f"espera... você tem {idade} anos???? como que tu consegue nadar com essa idade?\nJa descobriram a formula da imortalidade? kkkkkkkk")

