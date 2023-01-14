import os

os.system('cls')

# Cores e estilos
print('\nCores e Estilos\n')


'''comando \033[0;30;40m
0 ao 3 para normal, negrito, itálico e sublinhado, respectivamente
30 ao 39 cores da letras
40 ao 49 cores do fundo
Para que as cores fiquem apenas no 
elemento que vc quer, ao final 
add \033[m'''

cinza = '\033[1;30m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
lilas = '\033[1;35m'
azul = '\033[1;36m'
branco = '\033[1;37m'

print('Fonte colorida')

print(cinza+'Hello, mundo! 30 cinza')
print(vermelho+'Hello, mundo! 31 vermelho')
print(verde+'Hello, mundo! 32 verde')
print(amarelo+'Hello, mundo! 33 amarelo')
print(azul+'Hello, mundo! 34 azul')
print(lilas+'Hello, mundo! 35 lilás')
print(azul+'Hello, mundo! 36 azul claro')
print(branco+'Hello, mundo! 37 branco')

fundo_preto = '\033[0;40m'
fundo_vermelho = '\033[0;41m'
fundo_verde = '\033[0;42m'
fundo_amarelo = '\033[0;43m'
fundo_azul = '\033[0;44m'
fundo_lilas = '\033[0;45m'
fundo_azul_claro = '\033[0;46m'
fundo_cinza = '\033[0;47m'

print('\nFundo colorido')

print(fundo_preto+'Hello, mundo! 40 preto')
print(fundo_vermelho+'Hello, mundo! 41 vermelho')
print(fundo_verde+'Hello, mundo! 42 verde')
print(fundo_amarelo+'Hello, mundo! 43 amarelo')
print(fundo_azul+'Hello, mundo! 44 azul')
print(fundo_lilas+'Hello, mundo! 45 lilás')
print(fundo_azul_claro+'Hello, mundo! 46 azul claro')
print(fundo_cinza+'Hello, mundo! 47 cinza')

print('\n\033[1;34;42mFonte e Fundo')
print('\033[1;35;43mHello, mundo!')
