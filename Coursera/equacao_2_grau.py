# esse código calcula as raízes de uma equação de segundo grau a partir das constantes informadas pelo usuário

import math

def imprime_raizes(a, b, delta):
    if delta < 0:
        print('\nEsta equação não possui raízes reais.')
    else:
        if delta == 0:
            raiz = -b / (2 * a)
            print(f'\nA raiz desta equação é {raiz:.2f}')
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f'\nAs raízes da equação são {raiz1:.2f} e {raiz2:.2f}')

def delta(a, b, c):
    return (b ** 2) - (4 * a * c)

if (__name__ == '__main__'):
    a = float(input('Entre com a constante a: '))
    b = float(input('Entre com a constante b: '))
    c = float(input('Entre com a constante c: '))
    delta = delta(a, b, c)
    imprime_raizes(a, b, delta)
