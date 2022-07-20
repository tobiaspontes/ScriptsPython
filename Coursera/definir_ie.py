'''Este código recebe um número de IE informado pelo usuário
e retorna os dígitos correspondentes à centena de milhar e dezena de milhar
que são utilizados para definir qual IF deve cuidar do trabalho fiscal baseado na IE'''

def cria_lista(x):
    lista = []
    for i in range(12):
        lista.append(x % 10) # dividindo o nro por 10 e colocando o resto na lista
        x = x // 10 # dividindo o nro por 10 e ficando com a parte inteira do resultado
        i += 1
    return lista

def gera_dezena(lista):
    dezena = ''
    for i, digito in enumerate(lista):
        if (i == 4):
            dezena_milhar = str(digito)
        elif (i == 5):
            centena_milhar = str(digito)
    dezena = centena_milhar + dezena_milhar
    return dezena

def imprime_mensagens(x, dezena):
    print(f'\nA Inscrição Estadual digitada foi {x:,}'.replace(',','.'))
    print('\nO número para definir a IF é {}'.format(dezena))
    print('\nEntre 00 e 49: IF 1      Entre 50 e 99: IF 2')
    if (dezena <= '49'):
        print('\nA Inspetoria Fiscal responsável pelo trabalho é a IF 1')
    else:
        print('\nA Inspetoria Fiscal responsável pelo trabalho é a IF 2')

if (__name__ == '__main__'):
    ie = input('\nDigite a IE: ')
    if (len(ie) != 12):
        print('Erro! Número da IE não tem doze dígitos!')
        exit()
    x = int(ie)
    lista = cria_lista(x)
    dezena = gera_dezena(lista)
    imprime_mensagens(x, dezena)
