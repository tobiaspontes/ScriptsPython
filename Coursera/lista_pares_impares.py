# Este código gera uma lista de números inteiros aleatórios e cria duas listas
# uma lista de números pares e outra de números ímpares

from gera_lista import Lista

def cria_lista_pares_impares(numeros):
    pares = [x for x in numeros if x % 2 == 0]
    impares = [x for x in numeros if not x % 2 == 0]
    return [pares, impares]

def imprime_mensagens(lista_numeros, resultado):
    print('\nQtde de números lista original = ', len(lista_numeros), ':', '{}'.format(lista_numeros))
    print('\nQtde de pares digitados = ', len(resultado[0]),':','{}'.format(resultado[0]))
    print('\nQtde de ímpares digitados = ', len(resultado[1]),':','{}\n'.format(resultado[1]))

if (__name__ == '__main__'):
    n = int(input('\nQuantos números na lista? '))
    limite_inferior = int(input('Qual o limite inferior? '))
    limite_superior = int(input('Qual o limite superior? '))
    lista_numeros = Lista(n, limite_inferior, limite_superior)
    resultado = cria_lista_pares_impares(lista_numeros.lista)
    imprime_mensagens(lista_numeros.lista, resultado)