# esse código verifica se um número inteiro digitado pelo usuário é par ou ímpar

def verifica_par_ou_impar(x):
	resto = x % 2
	if resto == 0:
		print('O número digitado {} é par.'.format(x))
	else:
		print('O número digitado {} é ímpar.'.format(x))

if (__name__ == '__main__'):
	x = int(input('Digite um número inteiro: '))
	verifica_par_ou_impar(x)