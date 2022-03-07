def é_hipotenusa(x):
    c1 = 1
    c2 = 1
    while c1 < x:
        while c2 < x:
            if x**2 == c1**2 + c2**2:
                return True
            c2 = c2 + 1
        c2 = 1
        c1 = c1 + 1

def soma_hipotenusas(n):
    soma = 0
    i = 1
    while i <= n:
        if é_hipotenusa(i):
            soma = soma + i
        i = i + 1
    return soma
