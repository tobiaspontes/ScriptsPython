# esse código gera uma lista com números inteiros aleatórios entre 1 e 1000

import random

def mensagem_inicial():
    print()
    print(55 * '*')
    print(9 * '*', 'Lista de Números Inteiros Aleatória', 9 * '*')
    print('*', 51 * ' ', '*')
    print('** Os números gerados estão no intervalo de 1 a 1000 **')
    print('*', 51 * ' ', '*')
    print(55*'*')

def gera_numeros():
    lista_numeros = []
    n = int(input('\nQuantos números na lista?: '))
    i = 1
    while i <= n:
        numero = random.randrange(1, 1001)
        lista_numeros.append(numero)
        i += 1
    return lista_numeros

if (__name__ == '__main__'):
    mensagem_inicial()
    lista_numeros = gera_numeros()
    print('\nA lista gerada é: {}\n'.format(lista_numeros))