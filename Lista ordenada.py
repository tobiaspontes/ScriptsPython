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
print('\n\033[1;32mVamos criar uma lista'+'\n')
x = int(input('Digite um número ou zero para terminar: '))

lista=[]

while x != 0:
    lista.append(x)
    x = int(input('Digite um número ou zero para terminar: '))

# Verificando se a lista está em ordem crescente
if verifica_ordem(lista):
    print('\n\033[1;33mA lista está em ordem crescente.')
else:
    print('\n\033[1;33mA lista não está em ordem crescente.')

# Imprime lista original
print(f'\n\033[0;35mLista original:{lista:}')

# Classifica a lista em ordem crescente
lista.sort()
print(f'\n\033[0;37mLista em ordem crescente:{lista:}')

# Classifica a lista em ordem decrescente
lista.sort(reverse=True)
print(f'\n\033[0;36mLista em ordem decrescente:{lista:}\n')
