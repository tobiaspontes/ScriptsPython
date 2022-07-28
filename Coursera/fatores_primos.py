# Este programa retorna os fatores primos e sua multiplicidade de
# determinado número.
# Por exemplo: 1000 pode ser representado por 2*2*2*5*5*5.
# 1000 tem dois fatores primos: 2 com multiplicidade 3
# e 5 com multiplicidade 3.

def fator_primo(n):
    fator = 2
    multiplicidade = 0
    while n > 1:
        while n % fator == 0:   #verifica se resto da divisão é zero
            multiplicidade += 1
            n = n / fator
        if multiplicidade > 0:
            print(f'Fator = {fator:,.0f}  Multiplicidade = {multiplicidade}\n'.replace(',','.'))
        fator += 1
        multiplicidade = 0

if (__name__ == '__main__'):
    nro = int(input('\nDigite um número inteiro > 1: '))
    print(f'\nO número digitado foi {nro:,.0f}\n'.replace(',','.'))
    fator_primo(nro)
