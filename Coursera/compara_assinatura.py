def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    somatorio = 0
    grau = 0
    i = 0
    while i < 6:
        somatorio = somatorio + abs(as_a[i] - as_b[i])
        i = i + 1
    grau = somatorio / 6
    print('Grau de similaridade = ', grau)
