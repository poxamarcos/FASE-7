#FAÇA UM PROGRAMA QUE LEIA UM NUMERO E CALCULE 5% DE DESCONTO

n1 = int(input('Qual o valor do produto? '))
n2 = 5 * n1
n3 = n2 / 100
n4 = n1 + n3
print('O valor com o desconto incluso é igual a: {}'.format(n4))