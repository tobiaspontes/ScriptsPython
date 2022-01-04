'''Este código recebe um número inteiro informado pelo usuário
e retorna os dígitos correspondentes à unidade, dezena, centena etc do número'''

def obter_digito(d):
    if d == 0: return 'Unidade            '
    if d == 1: return 'Dezena             '
    if d == 2: return 'Centena            '
    if d == 3: return 'Milhar             '
    if d == 4: return 'Dezena de milhar   '
    if d == 5: return 'Centena de milhar  '
    if d == 6: return 'Milhão             '
    if d == 7: return 'Dezena de milhão   '
    if d == 8: return 'Centena de milhão  '
    if d == 9: return 'Bilhão             '
    
print('\n\033[1;32mDecomposição')
numero = input('\nDigite um número: ')
tamanho = len(numero)
x = int(numero)
lista = []
print(f'\n\033[0;33mO número digitado foi {x:,}\n'.replace(',','.'))
for i in range(tamanho):
    lista.append(x % 10) # dividindo o nro por 10 e colocando o resto na lista
    x = x // 10 # dividindo o nro por 10 e ficando com a parte inteira do resultado
    i += 1
for i, digito in enumerate(lista):
    print(obter_digito(i)+' =', digito)