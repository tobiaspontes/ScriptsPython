''' Calcula o fatorial de um número apresentado pelo usuário '''
def fat(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

n = int(input('Digite um número inteiro positivo; para terminar digite um número negativo: '))
while n >= 0:
    print('O fatorial é:', fat(n))
    n = int(input('Digite um número inteiro positivo; para terminar digite um número negativo: '))
