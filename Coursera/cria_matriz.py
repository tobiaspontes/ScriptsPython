# Este código cria uma matriz a partir de dados informados pelo usuário

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i+1) + '][' + str(j+1) + ']: '))
            linha.append(valor)
        matriz.append(linha)
    print()
    return matriz

def imprime_matriz(matriz):
    ''' Esta função imprime uma matriz linha por linha'''
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if j == num_colunas - 1:
                print(matriz[i][j], end = '')
            else:
                print(matriz[i][j],  end = ' ')
        print(end = '\n')


if (__name__ == '__main__'):
    lin = int(input('\nDigite o nro de linhas da matriz: '))
    col = int(input('\nDigite o nro de colunas da matriz: '))
    print()
    m = cria_matriz(lin, col)
    # for i in range(lin):
    #     print(m[i],  end = '\n')
    # print()
    imprime_matriz(m)