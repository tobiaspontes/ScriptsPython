# esse código gera uma lista de números inteiros; verifica se está em ordem crescente;
# gera duas novas listas: uma crescente e outra descrescente, preservando a lista original;
# o método sort() classifica e modifica a lista original sem criar nova lista;
# exemplo: lista.sort() é a mesma lista classificada em ordem ascendente e modificada.
# já a função sorted() classifica e cria nova lista.

import gera_lista_numeros_inteiros

def verifica_ordem(lista):
    crescente = True
    nro_anterior = 0
    for nro in lista:
        if nro < nro_anterior:
            crescente = False
        nro_anterior = nro
    return crescente

def gera_listas_classificadas(lista):
    listas_classificadas = []
    lista_crescente = sorted(lista)
    lista_decrescente = sorted(lista, reverse=True)
    listas_classificadas.append(lista_crescente)
    listas_classificadas.append(lista_decrescente)
    return listas_classificadas

def imprime_mensagens(lista, listas_classificadas):
    print(f'Lista original:{lista:}')
    print(f'Lista em ordem crescente:{listas_classificadas[0]:}')
    print(f'Lista em ordem decrescente:{listas_classificadas[1]:}')

if (__name__ == '__main__'):
    lista = gera_lista_numeros_inteiros.gera_numeros()
    if verifica_ordem(lista):
        print('\nA lista está em ordem crescente.')
    else:
        print('\nA lista não está em ordem crescente.')
    listas_classificadas = gera_listas_classificadas(lista)
    imprime_mensagens(lista, listas_classificadas)

