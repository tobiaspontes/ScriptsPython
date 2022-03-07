'''Este programa retorna os fatores primos e sua multiplicidade de
determinado número.
Por exemplo: 1000 pode ser representado por 2*2*2*5*5*5.
1000 tem dois fatores primos: 2 com multiplicidade 3
e 5 com multiplicidade 3.'''

n = int(input('Digite um número inteiro > 1: '))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:   #verifica se resto da divisão é zero
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print('fator', fator, 'multiplicidade =', multiplicidade)
    fator = fator + 1
    multiplicidade = 0
