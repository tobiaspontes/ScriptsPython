# Calcula o fatorial de um número apresentado pelo usuário

def fat(n):
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    return fatorial


if (__name__ == '__main__'):
    n = int(input('\nDigite um número inteiro positivo: '))
    print(f'\nO fatorial de {n} é igual a {fat(n):,.0f}\n'.replace(',','.'))