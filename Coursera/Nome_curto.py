def mais_curto(lista):
    ''' Esta função identifica o string mais curto de uma lista, ignorando espaços. '''
    tam_lista = len(lista)
    nome_curto = ''
    nome_sem_espaco = ''
    for i in range(tam_lista):
        nome_sem_espaco = lista[i].strip()
        if i == 0:
            nome_curto = nome_sem_espaco
        if len(nome_sem_espaco) < len(nome_curto):
            nome_curto = nome_sem_espaco
    print(nome_curto.capitalize())
