## Programa feito por Green em 2022, 
## para conclusão do Mundo 2 de Python no CEV

print("Empréstimo Bancário")
casa = float(input("Qual o valor da casa? \nR$  "))
salario = float(input("Qual o seu salário? \nR$  "))
parcelas = int(input("Em quantos anos você irá pagar? \n> "))
porcentagem_maxima_aceitavel = 30 # 30%

prestacao_anual = casa / (parcelas * 12)
salario_calculado = salario * (porcentagem_maxima_aceitavel / 100)

print(f"Com o salário de R$ {salario}, para comprar uma casa de R$ {casa}, em {parcelas} anos, é necessário pagar a prestação anual de {prestacao_anual}")


if salario_calculado > prestacao_anual:
    print("Emprestimo Aceito!")
else:
    print("Emprestimo Negado!")




