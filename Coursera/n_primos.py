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


def n_primos(n):
    ''' retorna a quantidade de números primos entre 2 e p número informado '''
    i = 2
    contador_primos = 0
    while i <= n:
        if éPrimo(i):
            contador_primos = contador_primos + 1
        i = i + 1
    return contador_primos

def main():
    numero = int(input('Digite um número inteiro: '))
    print('A quantidade de números primos entre 2 e', numero, 'é:', n_primos(numero))

main()