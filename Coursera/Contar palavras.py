''' Esta função conta o número de ocorrências de cada palavra em uma frase '''

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

# código principal
frase = 'O C6 Bank, em sua contestação, reconhece tratar-se de golpe corriqueiro e que com a entrada em vigor do PIX, houve maior vulnerabilidade no sistema de pagamentos e transferências de numerário. O que nos faz concluir que o banco deveria recrudescer seus mecanismos de detecção de fraudes, caso existam de fato, e agir prontamente quando qualquer irregularidade ou suspeita lhe fosse comunicada. Infelizmente, não foi o que ocorreu no presente caso.'
count_words(frase)
