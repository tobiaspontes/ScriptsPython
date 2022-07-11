# esse código pede ao usuário para digitar números inteiros e cria uma lista; digitar zero termina o processo

def gera_numeros():
    terminou = False
    lista_numeros = []

    while (not terminou):
        n = int(input('Digite um número inteiro, ou zero para terminar: '))
        if n == 0:
            terminou = True
        else:
            lista_numeros.append(n)
    return lista_numeros

if (__name__ == '__main__'):
    lista_numeros = gera_numeros()
    print(lista_numeros)