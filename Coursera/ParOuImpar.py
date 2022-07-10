# esse código verifica se um número inteiro digitado pelo usuário é par ou ímpar

def main():
	x = int(input('Digite um número inteiro: '))
	return x

def verifica_par_ou_impar(x):
	y = x % 2
	if y == 0:
		print('O número digitado {} é par.'.format(x))
	else:
		print('O número digitado {} é ímpar.'.format(x))

if (__name__ == '__main__'):
	x = main()
	verifica_par_ou_impar(x)