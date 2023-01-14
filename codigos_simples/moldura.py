import os

os.system('cls')

moldura = input('Digite um caracter para emoldurar a saída: ')

linha1 = '\n' + 20 * moldura + ' ' + 20 * moldura
linha2 = '\n' + 15 * moldura + 11 * ' ' + 15 * moldura
linha3 = '\n' + 10 * moldura + 21 * ' ' + 10 * moldura
linha4 = '\n' + 5 * moldura + 31 * ' ' + 5 * moldura
linha5 = '\n' + 7 * ' ' + 'JOÃO TOBIAS DA SILVA PONTES' + 7 * ' '

print(linha1, linha2, linha3, linha4, linha5, linha4, linha3, linha2, linha1)
print()

# moldura = 10 * '*'
# print('\n', moldura, input('Digite seu nome: '), moldura, '\n', moldura, 'Seja bem-vindo!', moldura)