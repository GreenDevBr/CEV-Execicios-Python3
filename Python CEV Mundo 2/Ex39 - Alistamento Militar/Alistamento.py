from datetime import date

ano = int(input("Digite o seu ano de nascimento: "))
idade = int(date.today().year) - ano

if idade < 17:
    print(f"Você deverá se alistar em {(18-idade)+date.today().year}")
elif idade == 17:
    print(f"Vocẽ ja pode se alistar, mas ainda não é obrigatório! Apenas no ano que vem ({date.today().year + 1})")
elif idade == 18:
    print("Com 18 anos, você deve se alistar o quanto antes! é OBRIGATÓRIO!")
elif idade >= 19:
    print(f"O seu ano de alistamento ja passou, há {idade-18} anos atras (em {date.today().year-(idade-18)}), deve comparecer ao alistamento!")
