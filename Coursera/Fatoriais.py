# Calcula o fatorial de um número apresentado pelo usuário

def fat(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial


if (__name__ == '__main__'):
    n = int(input('\nDigite um número inteiro positivo; para terminar digite um número negativo: '))
    while n >= 0:
        print(f'O fatorial de {n} é {fat(n):,.0f}'.replace(',','.'))
        n = int(input('\nDigite um número inteiro positivo; para terminar digite um número negativo: '))
