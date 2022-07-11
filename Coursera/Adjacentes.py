# esse código pede ao usuário para digitar um número inteiro e verifica se existem dígitos iguais adjacentes

def compara_digitos(digito_anterior, numero_anterior, tamanho):
	encontrei_adjacente = False
	i = 0
	lista = []
	while i < tamanho and tamanho > 1:
		digito = numero_anterior % 10
		if digito == digito_anterior:
			encontrei_adjacente = True
			lista.append(digito)
		numero_anterior = numero_anterior // 10
		digito_anterior = digito
		i = i + 1
	return [encontrei_adjacente, lista]

def imprime_mensagem(resultado):
	if resultado[0]:
		print('Sim, existem dígitos adjacentes:', resultado[1])
	else:
		print('Não existem dígitos adjacentes.')

if (__name__ == '__main__'):
	x = input('Digite um número inteiro: ')
	tamanho = len(x)
	y = int(x)
	digito_anterior = y % 10
	numero_anterior = y // 10
	resultado = compara_digitos(digito_anterior, numero_anterior, tamanho)
	imprime_mensagem(resultado)
