x = int(input('Digite um número inteiro: '))
y = x % 3
w = x % 5
if y == 0 and w == 0:
	print('FizzBuzz')
else:
	print(x)