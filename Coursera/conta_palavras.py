''' Esta função conta o número de ocorrências de cada palavra em uma frase.
    Qualquer caracter na lista .:!&@$%^&" é eliminado.
    Qualquer caracter na lista \n\r\t,_" é substituído por espaço em branco.
    Gera um dicionário com palavra(key) e quantidade de ocorrência no texto(value).
    A expressão resultado.keys() retorna as chaves do dicionário (palavras).
    A expressão resultado.values() retorna as quantidades de ocorrência de cada palavra.
    A expressão resultado.items() retorna chave e valor (palavra e quantidade de ocorrência).   '''

def count_words(sentence):
    for s in ".:!&@$%^&":  sentence=sentence.replace(s,'')
    for s in "\n\r\t,_":   sentence=sentence.replace(s,' ')
    counts={}

    for word in sentence.lower().split():
        word = word.strip('\'')
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

if (__name__ == '__main__'):
    frase = input('\nDigite o texto: ')
    resultado = count_words(frase)
    for palavra, qtde in resultado.items():
        complemento = 'vez'
        if qtde > 1:
            complemento = 'vezes'
        print('{}: {} {}'.format(palavra, qtde, complemento))
