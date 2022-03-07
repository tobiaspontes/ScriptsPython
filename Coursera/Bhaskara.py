def main():
        '''
        Função principal do programa: pede ao usuário os coeficientes
        da equação de segundo grau
        '''
        a = float(input('Entre com a constante a: '))
        b = float(input('Entre com a constante b: '))
        c = float(input('Entre com a constante c: '))
        imprime_raizes(a, b, c)

        
def imprime_raizes(a, b, c):
        '''
        Função que calcula e imprime as raízes
        '''
        import math
        d = Delta(a, b, c)
        if d < 0:
                print('\nEsta equação não possui raízes reais.')
        else:
                if d == 0:
                        raiz1 = -b / (2 * a) 
                        print(f'\nA raiz desta equação é {raiz1:.2f}')
                else:
                        raiz1 = (-b + math.sqrt(d)) / (2 * a)
                        raiz2 = (-b - math.sqrt(d)) / (2 * a)
                        if raiz1 < raiz2:
                                print(f'\nAs raízes da equação são {raiz1:.2f} e {raiz2:.2f}')
                        else:
                                print(f'\nAs raízes da equação são {raiz2:.2f} e {raiz1:.2f}')

                                
def Delta(a, b, c):
    '''
    Função que retorna o delta da fórmula de Bhaskara.
    '''
    return (b ** 2) - (4 * a * c)


# código principal
main()
