# esse código pede ao usuário para digitar números inteiros; quando digitar zero cessa a entrada de dados
# gera uma lista com os números digitados; e a partir dessa lista, cria outras duas: uma de números pares e outra de
# números ímpares

import gera_lista_numeros_inteiros

def cria_lista_pares_impares(numeros):
    pares = [x for x in numeros if x % 2 == 0]
    impares = [x for x in numeros if not x % 2 == 0]
    return [pares, impares]

def imprime_mensagens(resultado):
    print('Qtde de pares digitados = ', len(resultado[0]),':','{}'.format(resultado[0]))
    print('Qtde de ímpares digitados = ', len(resultado[1]),':','{}'.format(resultado[1]))

if (__name__ == '__main__'):
    lista_numeros = gera_lista_numeros_inteiros.gera_numeros()
    resultado = cria_lista_pares_impares(lista_numeros)
    imprime_mensagens(resultado)