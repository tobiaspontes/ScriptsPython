x = input('Digite um número inteiro: ')
tamanho = len(x)
y = int(x)
guardaDigitoAnterior = y % 10
guardaNumeroAnterior = y // 10
encontreiAdjacente = False
i = 0
while i < tamanho and tamanho > 1:
	guardaDigito = guardaNumeroAnterior % 10
	if guardaDigito == guardaDigitoAnterior:
		encontreiAdjacente = True
	guardaNumeroAnterior = guardaNumeroAnterior // 10
	guardaDigitoAnterior = guardaDigito
	i = i + 1
if encontreiAdjacente:
	print('Sim, existem dígitos adjacentes.')
else:
	print('Não existem dígitos adjacentes.')	
