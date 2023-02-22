# Verificar se uma lista está em ordem crescente. Classificar uma lista.
import os


def cria_lista():
    # Criando uma lista
    print(f'\n{verde}Vamos criar uma lista\n')
    x = int(input('Digite um número ou zero para terminar: '))
    global lista   # indica que lista é uma variável global (pode ser acessada em qualquer parte do código)
    lista=[]
    while x != 0:
        lista.append(x)
        x = int(input('Digite um número ou zero para terminar: '))
    return lista


def verifica_ordem(lista):
    crescente = True
    nro_anterior = 0
    for nro in lista:
        if nro < nro_anterior:
            crescente = False
        nro_anterior = nro
    return crescente


def imprime_lista(lista):
    # Imprime lista original
    print(f'\n{rosa}Lista original:{lista:}')
    # Classifica a lista em ordem crescente
    lista.sort()
    print(f'\n{branco}Lista em ordem crescente:{lista:}')
    # Classifica a lista em ordem decrescente
    lista.sort(reverse=True)
    print(f'\n{azul}Lista em ordem decrescente:{lista:}\n')


if __name__ == '__main__':
    # definições iniciais
    os.system('cls')
    verde = '\033[1;32m'
    amarelo = '\033[1;33m'
    rosa = '\033[0;35m'
    branco = '\033[0;37m'
    azul = '\033[0;36m'

    cria_lista()
    # Verifica se a lista está em ordem crescente
    if verifica_ordem(lista):
        print(f'\n{amarelo}A lista está em ordem crescente.')
    else:
        print(f'\n{amarelo}A lista não está em ordem crescente.')   
    imprime_lista(lista)