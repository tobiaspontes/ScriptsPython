def soma_matrizes(m1, m2):
    ''' Esta função soma duas matrizes se tiverem a mesma dimensão'''
    l1 = len(m1)
    c1 = len(m1[0])
    l2 = len(m2)
    c2 = len(m2[0])
    matriz=[]
    if l1 == l2 and c1 == c2:
        for i in range(l1):
            linha=[]
            for j in range(c1):
                valor = m1[i][j] + m2[i][j]
                linha.append(valor)
            matriz.append(linha)
        return matriz
    return False
