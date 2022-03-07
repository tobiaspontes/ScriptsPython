def Fatorial(n):
        if n == 0:
                saida = 1
        else:
                saida = n
                while n > 1:
                        saida = saida * (n - 1)
                        n = n - 1
        return saida


def Combinacao (n , k):
    c = Fatorial(n) / (Fatorial(k) * Fatorial(n - k))
    return c

def Arranjo (n, k):
        a = Fatorial(n) / Fatorial(n - k)
        return a

