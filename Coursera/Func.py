def soma(x, y):
    '''
    Função recebe os parâmetros x e y e retorna a soma dos parâmetros
    '''
    z = x + y
    return z

def Fatorial(n):
    '''
    Função recebe um número inteiro e devolve seu fatorial
    '''
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

def Combinacao (n , k):
    '''
    Função que retorna a quantidade de combinações de n elementos
    tomados k a k.
    Na combinação, a ordem dos elementos não importa: (a,b) = (b,a).
    '''
    c = Fatorial(n) // (Fatorial(k) * Fatorial(n - k))
    return c

def Arranjo (n, k):
    '''
    Função que retorna a quantidade de arranjos de n elementos
    tomados k a k.
    No arranjo, a ordem dos elementos importa: (a,b) <> (b,a).
    '''
    a = Fatorial(n) // Fatorial(n - k)
    return a

def Delta(a, b, c):
    '''
    Função que retorna o delta da fórmula de Bhaskara.
    '''
    return (b ** 2) - (4 * a * c)

def Raiz(texto, a, b, c):
    '''
    Função que calcula as raízes de equação de segundo grau
    utilizando a fórmula de Bhaskara.
    '''
    import math
    if texto == 'raiz única':
        return -b / (2 * a)
    if texto == 'soma':
        return (-b + math.sqrt(Delta(a, b, c))) / (2 * a)
    if texto == 'subtração':
        return (-b - math.sqrt(Delta(a, b, c))) / (2 * a)

def RaizEquacao(a, b, c):
    '''
    Função que retorna as raízes de uma equação de segundo grau.
    '''
    if Delta(a, b, c) < 0:
            return print("esta equação não possui raízes reais")
    else:
            if Delta(a, b, c) == 0:
                    texto = 'raiz única'
                    return print("a raiz desta equação é",Raiz(texto, a, b, c))
            else:
                    texto = 'soma'
                    x1 = Raiz(texto, a, b, c)
                    texto = 'subtração'
                    x2 = Raiz(texto, a, b, c)
                    if x1 < x2:
                            return print("as raízes da equação são", x1,"e", x2)
                    else:
                            return print("as raízes da equação são", x2,"e", x1)

