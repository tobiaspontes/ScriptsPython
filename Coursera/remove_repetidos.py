def remove_repetidos(lista):
    lista2 = []
    for x in range(len(lista)):
        if lista[x] not in lista2:
            lista2.append(lista[x])    
    return sorted(lista2)
