def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ',mínima(temperaturas), 'C.')
    print('A maior temperatura do mês foi: ',máxima(temperaturas), 'C.')

def mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def teste_pontual(temp, valor_esperado_mínimo, valor_esperado_máximo):
    valor_calculado_mínimo = mínima(temp)
    valor_calculado_máximo = máxima(temp)
    if valor_calculado_mínimo != valor_esperado_mínimo or valor_calculado_máximo != valor_esperado_máximo:
        print('Valor errado para array ', temp)
        print('Valor esperado mínimo: ', valor_esperado_mínimo, ', Valor calculado: ', valor_calculado_mínimo)
        print('Valor esperado máximo: ', valor_esperado_máximo, ', Valor calculado: ', valor_calculado_máximo)
        
def testa_minmax():
    print('Iniciando os testes')
    lista1 = [[0], [0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [25, 93, 28, 22, 36, 24, 23, 30], [10, 25, 22, -1, 0, -10]]
    lista2 = [0, 0, 0, 22, -10]
    lista3 = [0, 0, 10, 93, 25]
    i = 0
    while i < len(lista1):
        teste_pontual(lista1[i], lista2[i], lista3[i])
        i = i + 1
    print('Finalizando os testes')


'''
    teste_pontual([0], 0, 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0, 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10)
    teste_pontual([25, 93, 28, 22, 36, 24, 23, 30], 22, 93)
    teste_pontual([10, 25, 22, -1, 0, -10], -10, 25)
'''
