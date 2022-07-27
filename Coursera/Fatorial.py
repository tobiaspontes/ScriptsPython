n = int(input('\nDigite o valor de n: '))
if n == 0:
	saida = 1
else:
	saida = n
	while n > 1:
		saida = saida * (n - 1)
		n = n - 1
print(f'\nO fatorial é {saida:,.0f}\n'.replace(',','.'))