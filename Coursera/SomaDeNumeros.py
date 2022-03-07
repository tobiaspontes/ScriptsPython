
i = int(input('Quantos números tem a sequência que você quer somar? '))
soma = 0
k = 1
while k <= i:
	valor = int(input('Digite valor a ser somado: '))
	soma = soma + valor
	k = k + 1
print('A soma dos valores digitados é:', soma)