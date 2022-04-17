# FAÇA UM PROGRAMA QUE LEIA UM NUMERO E MOSTRE O DOBRO, SEU TRIPLO E SUA RAIZ QUADRADA

n1 = int(input('Insira um número: '))

dobro = n1*2
triplo = n1*3
raiz = n1 ** (1/2)

print('O número inserido foi: {}\n o seu dobro é: {}\n seu triplo: {}\n e sua raiz quadrada é: {:.3f}'.format(n1, dobro, triplo,raiz))