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

    print('\nQtde de caracteres: ', qtde_caracteres)

# código principal
texto = 'O C6 Bank, em sua contestação, reconhece tratar-se de golpe corriqueiro e que com a entrada em vigor do PIX, houve maior vulnerabilidade no sistema de pagamentos e transferências de numerário. O que nos faz concluir que o banco deveria recrudescer seus mecanismos de detecção de fraudes, caso existam de fato, e agir prontamente quando qualquer irregularidade ou suspeita lhe fosse comunicada. Infelizmente, não foi o que ocorreu no presente caso.'
ind = 'frase'
print('\n'+texto)
conta_caracteres(texto, ind)
