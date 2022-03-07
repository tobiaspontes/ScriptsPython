import re

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    print('lista de frases: ', re.split(r'[,:;]+', sentenca))
