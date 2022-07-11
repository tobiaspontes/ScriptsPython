# esse código gera uma lista de números ímpares a partir da quantidade informada pelo usuário

def gera_impares(n):
	lista_impares = []
	i = 1
	k = 1
	while k <= n:
		lista_impares.append(i)
		i = i + 2
		k = k + 1
	return lista_impares

def imprime_resultado(n, lista_impares):
	k = 1
	i = 0
	while k <= n:
		print('(', k, ')', ' ', lista_impares[i], sep='')
		k += 1
		i += 1

if (__name__ == '__main__'):
	n = int(input('Digite a quantidade de números ímpares desejada: '))
	lista_impares = gera_impares(n)
	imprime_resultado(n, lista_impares)

