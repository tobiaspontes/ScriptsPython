def sao_multiplicaveis(m1, m2):
    ''' Esta função verifica se duas matrizes são multiplicáveis.
        Duas matrizes são multiplicáveis se o número de colunas da primeira
        é igual ao número de linhas da segunda.'''
    num_colunas = len(m1[0])
    num_linhas = len(m2)
    if num_colunas == num_linhas:
        return True
    else:
        return False
