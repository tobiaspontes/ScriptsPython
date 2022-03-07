import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    somatorio = 0
    i = 0
    while i < 6:
        somatorio = somatorio + abs(as_a[i] - as_b[i])
        i = i + 1
    grau = somatorio / 6
    return grau

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
 
    lista_palavras = []
    lista_frases = []
    lista_sentencas = separa_sentencas(texto)

    numero_caracteres_sentenca =  conta_caracteres(texto, 'sentença')
    numero_caracteres_frase = conta_caracteres(texto, 'frase')
    numero_caracteres_palavra = conta_caracteres(texto, 'palavra')
    
    sentencas = separa_sentencas(texto)
    
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        lista_frases.extend(frases)
        for frase in frases:
            palavras = separa_palavras(frase)
            lista_palavras.extend(palavras)
    
    ''' Primeiro item da assinatura: tamanho médio da palavra (tmp) '''
    tmp = tamanho_medio_de_palavra(numero_caracteres_palavra, lista_palavras)

    ''' Segundo item da assinatura: relação type-token (rtt) '''
    rtt = relacao_type_token(lista_palavras, n_palavras_diferentes)

    ''' Terceiro item da assinatura: razão hapax legomana (rhl) '''
    rhl = razao_hapax_legomana(lista_palavras, n_palavras_unicas)

    ''' Quarto item da assinatura: tamanho médio da sentença (tms) '''
    tms = tamanho_medio_de_sentenca(numero_caracteres_sentenca, lista_sentencas)

    ''' Quinto item da assinatura: complexidade média da sentença (cms) '''
    cms = complexidade_de_sentenca(lista_frases, lista_sentencas)

    ''' Sexto item da assinatura: tamanho médio da frase (tmf) '''
    tmf = tamanho_medio_de_frase(numero_caracteres_frase, lista_frases)
    
    assinatura = [tmp, rtt, rhl, tms, cms, tmf]
    
    return assinatura

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
    
def tamanho_medio_de_palavra(numero_caracteres, lista_palavras):
    return numero_caracteres / len(lista_palavras)

def relacao_type_token(lista_palavras, n_palavras_diferentes):
    return n_palavras_diferentes(lista_palavras) / len(lista_palavras)

def razao_hapax_legomana(lista_palavras, n_palavras_unicas):
    return n_palavras_unicas(lista_palavras) / len(lista_palavras)

def tamanho_medio_de_sentenca(numero_caracteres, lista_sentencas):
    return numero_caracteres / len(lista_sentencas)

def complexidade_de_sentenca(lista_frases, lista_sentencas):
    return len(lista_frases) / len(lista_sentencas)

def tamanho_medio_de_frase(numero_caracteres, lista_frases):
    return numero_caracteres / len(lista_frases)
    

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    ass_texto = []
    lista_assinaturas = []
    grau = 0
    n = 0
    i = 0
    while i < len(textos):
        ass_texto = calcula_assinatura(textos[i])
        grau = compara_assinatura(ass_texto, ass_cp)
        lista_assinaturas.append(grau)
        ass_texto = []
        i = i + 1
    
    return menor_elemento(lista_assinaturas)

def menor_elemento(lista):
    '''Esta função identifica na lista_assinaturas o valor mínimo (texto com maior probabilidade de ter sido infectado) '''

    menor = 0
    i = 0
    k = 0
    
    while i < len(lista):
        if i == 0:
            menor = lista[i]
            k = i
        if lista[i] < menor:
            menor = lista[i]
            k = i
        i = i + 1

    return k + 1

def main():
    lista_textos = []
    ass_copiah = le_assinatura()
    lista_textos = le_textos()
    n = avalia_textos(lista_textos, ass_copiah)
    print
    print('O autor do texto ', n, ' está infectado com COH-PIAH')
    
