## FAÇA UM PROGRAMA QUE LEIA QUANTO DINHEIRO EM $ VC TEM E MOSTRE QUANTOS DOLARES VC PODE COMPRAR

n1 = float(input('Quanto dinheiro você tem ? R$: '))
print(f'Com R${n1}, você pode comprar:\nUS${n1/4.70 :.2f}\n€{n1/5.08 :.2f} ')