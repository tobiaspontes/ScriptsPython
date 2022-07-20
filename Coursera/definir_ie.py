# Este código recebe um número de IE informado pelo usuário.
# Retorna os dígitos correspondentes à centena de milhar e dezena de milhar,
# que são utilizados para definir qual IF deve cuidar do trabalho fiscal baseado na IE.
# A IE informada pela usuário deve ter 12 dígitos. Caso contrário, emite mensagem de erro.
# Transforma a entrada digitada em número e cria uma lista com os dígitos correspondentes.
# Com a lista criada, gera a dezena indicativa do Núcleo Fiscal responsável pelo trabalho.

def cria_lista(x):
    lista = []
    for i in range(12):
        lista.append(x % 10) # cada dígito é obtido pelo resto da divisão do nro por 10
        x = x // 10          # atualiza o número com a parte inteira da divisão por 10
        i += 1
    return lista

def gera_dezena(lista):
    dezena = str(lista[5]) + str(lista[4])
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
