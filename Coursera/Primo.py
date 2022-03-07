x = int(input('Digite um número inteiro: '))
i = 1
qtdeDivisores = 0
while i <= x:
	if x % i == 0:
		qtdeDivisores = qtdeDivisores + 1
	i = i + 1
if qtdeDivisores > 2 or x == 1:
	print(x, 'não é primo! Qtde de divisores:', qtdeDivisores)
else:
	print(x, 'é primo! Qtde de divisores:', qtdeDivisores)
