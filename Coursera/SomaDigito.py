x = input('Informe um número inteiro: ')
tamanho = len(x)
somadigito = 0
i = 0
y = int(x)
while i < tamanho:
	somadigito = somadigito + (y % 10)
	y = y // 10
	i = i + 1
print('A soma dos dígitos é', somadigito)
