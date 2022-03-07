def maior_primo(n):
    k = 2
    while k <= n:
        if primo(k) == 'primo':
            guarda_primo = k
        k = k + 1
    return guarda_primo

def primo(x):
    i = 1
    qtdeDivisores = 0
    while i <= x:
        if x % i == 0:
            qtdeDivisores = qtdeDivisores + 1
        i = i + 1
    if qtdeDivisores > 2 or x == 1:
        return 'não primo'
    else:
        return 'primo'
