dias = int(input('Quantos dias o carro foi alugado? :'))
percorreu = float(input('Quantos km o carro percorreu? :'))

print('O total a pagar é de R$:{:.2f}'.format(dias * 60 + percorreu * 0.15))