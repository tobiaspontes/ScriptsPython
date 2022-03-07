def maior_elemento(lista):
    for x in range(len(lista)):
        if x == 0:
            maior = lista[x]
        if lista[x] > maior:
            maior = lista[x]    
    return maior
