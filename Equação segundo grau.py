def main():
    '''
    Função principal do programa: pede ao usuário os coeficientes
    da equação de segundo grau
    '''
    a = float(input('\n\033[0;35mEntre com a constante a: '))
    b = float(input('\n\033[0;35mEntre com a constante b: '))
    c = float(input('\n\033[0;35mEntre com a constante c: '))
    imprime_raizes(a, b, c)

        
def imprime_raizes(a, b, c):
    '''
    Função que calcula e imprime as raízes
    '''
    import math
    d = Delta(a, b, c)
    if d < 0:
        print('\n\033[1;33mEsta equação não possui raízes reais.\n')
    else:
        if d == 0:
            raiz1 = -b / (2 * a) 
            print(f'\n\033[1;33mA raiz desta equação é {raiz1:.2f}\n')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            if raiz1 < raiz2:
                print(f'\n\033[1;33mAs raízes da equação são {raiz1:.2f} e {raiz2:.2f}\n')
            else:
                print(f'\n\033[1;33mAs raízes da equação são {raiz2:.2f} e {raiz1:.2f}\n')

                                
def Delta(a, b, c):
    '''
    Função que retorna o delta da fórmula de Bhaskara.
    '''
    return (b ** 2) - (4 * a * c)


# código principal
print('\n\033[1;32mEquação 2° grau')
main()
