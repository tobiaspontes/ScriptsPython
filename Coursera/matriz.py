# Cria uma matriz cujo valores são o produto do número da linha x o número da coluna.
# A matriz é uma lista onde cada elemento é uma lista. O tamanho da lista é a quantidade de linhas.

def cria_matriz(num_linhas, num_colunas):
    ''' Esta função cria uma matriz (num_linhas x num_colunas)
    e preenche com o valor dado pela multiplicação do número da linha pelo número da coluna.'''
    matriz = [] # lista vazia
    for i in range(num_linhas):
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append((i+1) * (1+j)) # valores da matriz: produto do número da linha x número da coluna
        matriz.append(linha) # adiciona linha à matriz
    return matriz

def dimensoes(matriz):
    ''' Esta função retorna as dimensões de uma matriz '''
    i = len(matriz)
    j = len(matriz[0])
    dimensao = (str(i) + 'X' + str(j))
    return dimensao


if (__name__ == '__main__'):
    nro_linhas = int(input('\nDigite o número de linhas: '))
    nro_colunas = int(input('Digite o número de colunas: '))
    print()

    # Chama a função
    matriz = cria_matriz(nro_linhas,nro_colunas)

    ''' Imprime a matriz '''
    print('A matriz tem dimensão:', dimensoes(matriz))
    for i in range(nro_linhas):
        print(matriz[i], end='\n')

    print('\nA matriz é uma lista:', matriz)
