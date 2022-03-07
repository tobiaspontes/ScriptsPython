""" Esta funççao recursiva implementa diretamente
    a definição indutiva da soma dos inteiros de 1 até N:
    a) A soma dos inteiros positivos até 1 é 1;
    b) a soma dos inteiros positivos de 1 até N é
       a soma de N com a soma dos inteiros positivos até N-1"""

def Soma1aN(N):
    if N==1: return(1)
    else: return (N+Soma1aN(N-1)) # note-se a ativação recursiva

# Uso da função
N=int(input('Entre com o valor de N: '))
print('A soma de 1 a', N, 'é', Soma1aN(N))
