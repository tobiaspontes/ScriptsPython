# Verificar se uma lista está em ordem crescente. Classificar uma lista.

def verifica_ordem(lista):
    crescente = True
    nro_anterior = 0
    for nro in lista:
        if nro < nro_anterior:
            crescente = False
        nro_anterior = nro
    return crescente

# Criando uma lista
print('\nVamos criar uma lista!'+'\n')
x = int(input('Digite um número ou zero para terminar: '))

lista=[]

while x != 0:
    lista.append(x)
    x = int(input('Digite um número ou zero para terminar: '))

# Verificando se a lista está em ordem crescente
if verifica_ordem(lista):
    print('\nA lista está em ordem crescente.')
else:
    print('\nA lista não está em ordem crescente.')

# Imprime lista original
print(f'\nLista original:{lista:}')

# Classifica a lista em ordem crescente
lista.sort()
print(f'\nLista em ordem crescente:{lista:}')

# Classifica a lista em ordem decrescente
lista.sort(reverse=True)
print(f'\nLista em ordem decrescente:{lista:}')

