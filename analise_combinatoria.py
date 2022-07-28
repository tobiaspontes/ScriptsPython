# Este código calcula fatorial, combinação e arranjo

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

def combinacao(n, k):
    # Função que retorna a quantidade de combinações de n elementos
    # tomados k a k.
    # Na combinação, a ordem dos elementos não importa: (a,b) = (b,a).
    c = fatorial(n) / (fatorial(k) * fatorial(n - k))
    return c

def arranjo(n, k):
    # Função que retorna a quantidade de arranjos de n elementos
    # tomados k a k.
    # No arranjo, a ordem dos elementos importa: (a,b) <> (b,a).
    a = fatorial(n) / fatorial(n - k)
    return a

if (__name__ == '__main__'):
    n = int(input('\nEntre com o número de elementos da análise: '))
    k = int(input('\nEntre com o número da combinação: '))
    print(f'\nA combinação de {n} elementos tomados {k} a {k} é igual a {combinacao(n,k):,.0f}'.replace(',','.'))
    print(f'\nO arranjo de {n} elementos tomados {k} a {k} é igual a {arranjo(n,k):,.0f}\n'.replace(',','.'))