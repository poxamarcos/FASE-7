n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor:'))

s = n1 + n2
m = n1* n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é: {}\n a multiplicação é: {}\n a divisão é: {:.3f}\n a divisão inteira é: {}\n a potência é: {}\n".format(s, m, d, di, e))
