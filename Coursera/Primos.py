def éPrimo(x):
    ''' primeiro testa se x = 2 (primo) '''
    if x == 2:
        return True
    ''' depois verifica se o resto da divisão do número por algum fator entre 2 e metade do número é zero '''
    fator = 2
    while x % fator != 0 and fator <= x / 2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input('Limite máximo: '))

n = 2
while n < limite:
    if éPrimo(n):
        print(n, end = ', ')
    n = n + 1
