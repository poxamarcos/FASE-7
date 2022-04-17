# FAÇA UM PROGRAMA QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE COM 15% DE AUMENTO

n1 = float(input('Qual o seu salario? R$: '))
n2 = n1 * 15 / 100
n3 = n1 + n2

print('O seu salario com o aumento de 15%, é: {:.3f}'.format(n3))