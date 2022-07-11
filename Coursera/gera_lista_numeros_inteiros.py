# esse código gera uma lista com números inteiros aleatórios

import random

def mensagem_inicial():
    print()
    print(55 * '*')
    print(9 * '*', 'Lista de Números Inteiros Aleatória', 9 * '*')
    print('*', 51 * ' ', '*')
    print('*   Informe quantidade, limites inferior e superior   *')
    print('*', 51 * ' ', '*')
    print(55*'*')

def gera_numeros(n, limite_inferior, limite_superior):
    lista_numeros = []
    i = 1
    while i <= n:
        numero = random.randrange(limite_inferior, limite_superior + 1)
        lista_numeros.append(numero)
        i += 1
    return lista_numeros

def verifica_erro(n, limite_inferior, limite_superior):
    intervalo = (limite_superior + 1) - limite_inferior
    if (intervalo <= 0):
        print('Limite superior deve ser maior do que limite inferior!')
        exit()
    if (n > intervalo):
        print('Quantidade de números solicitada é maior do que o intervalo!')
        exit()

if (__name__ == '__main__'):
    mensagem_inicial()
    n = int(input('\nQuantos números na lista? '))
    limite_inferior = int(input('Qual o limite inferior? '))
    limite_superior = int(input('Qual o limite superior? '))
    verifica_erro(n, limite_inferior, limite_superior)
    lista_numeros = gera_numeros(n, limite_inferior, limite_superior)
    print('\nA lista gerada é: {}\n'.format(lista_numeros))