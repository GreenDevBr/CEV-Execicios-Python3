import time
print('{:=^40}\n'.format('Numeros Pares'))
var = int(input('Contar ate o número: '))
for c in range(0, var+1, 2):
    print(c, end=" ")
print("\ne estes foram os números pares :)")