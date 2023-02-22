# Verifica dígitos adjacentes 
import os


def verifica_adjacente(y):
    guardaDigitoAnterior = y % 10
    guardaNumeroAnterior = y // 10
    encontreiAdjacente = False
    i = 0
    while i < tamanho and tamanho > 1:
        guardaDigito = guardaNumeroAnterior % 10
        if guardaDigito == guardaDigitoAnterior:
            encontreiAdjacente = True
        guardaNumeroAnterior = guardaNumeroAnterior // 10
        guardaDigitoAnterior = guardaDigito
        i = i + 1
    if encontreiAdjacente:
        print(f'\n{rosa}Sim, existem dígitos adjacentes.\n')
    else:
        print(f'\n{rosa}Não existem dígitos adjacentes.\n')	


if __name__ == '__main__':
    os.system('cls')
    verde = '\033[1;32m'
    rosa = '\033[1;35m'
    print(f'\n{verde}Dígitos adjacentes')
    x = input('\nDigite um número inteiro: ')
    tamanho = len(x)
    y = int(x)
    verifica_adjacente(y)