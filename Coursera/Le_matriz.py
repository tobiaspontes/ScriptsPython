def cria_matriz(num_linhas, num_colunas):
    ''' Esta função cria uma matriz (num_linhas x num_colunas)
    e preenche com o valor digitado pelo usuário.'''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        linha = [] # lista vazia
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + ']: '))
            linha.append(valor)
        matriz.append(linha) # adiciona linha à matriz
    ''' Imprime a matriz '''
    '''for i in range(num_linhas):
        print(matriz[i],  end = '\n')'''
    return matriz

def le_matriz():
    lin = int(input('Digite o nro de linhas da matriz: '))
    col = int(input('Digite o nro de colunas da matriz: '))
    m = cria_matriz(lin, col)
    ''' Imprime a matriz '''
    for i in range(lin):
        print(m[i],  end = '\n')
