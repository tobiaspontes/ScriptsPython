# esse código pede ao usuário para digitar números inteiros; quando digitar zero cessa a entrada de dados
# gera uma lista com os números digitados; e a partir dessa lista, cria outras duas: uma de números pares e outra de
# números ímpares

import gera_lista_numeros_inteiros

def cria_lista_pares(numeros):
    pares = [x for x in numeros if x % 2 == 0]
    return pares

def cria_lista_impares(numeros):
    impares = [x for x in numeros if not x % 2 == 0]
    return impares

def imprime_mensagens_pares(pares):
    print('Qtde de pares digitados = ', len(pares))
    print('Números pares: {}'.format(pares))

def imprime_mensagens_impares(impares):
    print('Qtde de ímpares digitados = ', len(impares))
    print('Números ímpares: {}'.format(impares))

if (__name__ == '__main__'):
    lista_numeros = gera_lista_numeros_inteiros.gera_numeros()
    pares = cria_lista_pares(lista_numeros)
    impares = cria_lista_impares(lista_numeros)
    imprime_mensagens_pares(pares)
    imprime_mensagens_impares(impares)