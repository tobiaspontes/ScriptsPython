def conta_caracteres(texto, ind):
    ''' Esta função conta o número de caracteres do texto, excluindo pontuação e quebra de linha '''

    ''' elimina as quebras de linhas'''
    texto = texto.replace("\n","")

    
    ''' se for sentença, elimina pontuação final (., !, ?)'''
    if ind == 'sentença':
        texto = texto.replace(".","")
        texto = texto.replace("!","")
        texto = texto.replace("?","")

    ''' se for frase, elimina toda pontuação, menos espaços em branco'''
    if ind == 'frase':
        texto = texto.replace(".","")
        texto = texto.replace("!","")
        texto = texto.replace("?","")
        texto = texto.replace(",","")
        texto = texto.replace(";","")
        texto = texto.replace(":","")

    ''' se for palavra, elimina espaços em branco e toda pontuação'''
    if ind == 'palavra':
        texto = texto.replace(" ","")
        texto = texto.replace(".","")
        texto = texto.replace("!","")
        texto = texto.replace("?","")
        texto = texto.replace(",","")
        texto = texto.replace(";","")
        texto = texto.replace(":","")
        
    qtde_caracteres = 0
    for caracter in texto:
       qtde_caracteres = qtde_caracteres + 1

    return qtde_caracteres

if (__name__ == '__main__'):
    texto = input('\nDigite o texto: ')
    ind = 'frase'
    qtde = conta_caracteres(texto, ind)
    print('\nQtde de caracteres: ', qtde)
