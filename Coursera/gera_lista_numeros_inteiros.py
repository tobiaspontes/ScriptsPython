# esse código gera uma lista com números inteiros aleatórios

from gera_lista import Lista

def mensagem_inicial():
    print()
    print(55 * '*')
    print(9 * '*', 'Lista de Números Inteiros Aleatória', 9 * '*')
    print('*', 51 * ' ', '*')
    print('*   Informe quantidade, limites inferior e superior   *')
    print('*', 51 * ' ', '*')
    print(55*'*')

if (__name__ == '__main__'):
    mensagem_inicial()
    n = int(input('\nQuantos números na lista? '))
    limite_inferior = int(input('Qual o limite inferior? '))
    limite_superior = int(input('Qual o limite superior? '))
    lista_numeros = Lista(n, limite_inferior, limite_superior)
    print('\nA lista gerada é: {}\n'.format(lista_numeros.lista))