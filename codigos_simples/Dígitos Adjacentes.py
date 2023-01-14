# Verifica dígitos adjacentes 
import os

os.system('cls')

print('\n\033[1;32mDígitos adjacentes')
x = input('\nDigite um número inteiro: ')
tamanho = len(x)
y = int(x)
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
    print('\n\033[1;35mSim, existem dígitos adjacentes.\n')
else:
    print('\n\033[1;35mNão existem dígitos adjacentes.\n')	
