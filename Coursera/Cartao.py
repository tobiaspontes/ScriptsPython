meuCartao = int(input('Digite o número de seu cartão: '))
cartaoLido = 1
encontreiMeuCartao = False
while cartaoLido != 0 and not encontreiMeuCartao:
	cartaoLido = int(input('Digite número do cartão: '))
	if cartaoLido == meuCartao:
		encontreiMeuCartao = True
if encontreiMeuCartao:
	print('Cartão encontrado!')
else:
	print('Cartão não localizado!')