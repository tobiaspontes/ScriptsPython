n = int(input('Digite o valor de n: '))
if n == 0:
	saida = 1
else:
	saida = n
	while n > 1:
		saida = saida * (n - 1)
		n = n - 1
print(saida)