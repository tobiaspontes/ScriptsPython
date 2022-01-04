# Cores e estilos
print('\nCores e Estilos\n')


'''comando \033[0;30;40m
0 ao 3 para normal, negrito, itálico e sublinhado, respectivamente
30 ao 39 cores da letras
40 ao 49 cores do fundo
Para que as cores fiquem apenas no 
elemento que vc quer, ao final 
add \033[m'''

fo30 = '\033[1;30m'
fo31 = '\033[1;31m'
fo32 = '\033[1;32m'
fo33 = '\033[1;33m'
fo34 = '\033[1;34m'
fo35 = '\033[1;35m'
fo36 = '\033[1;36m'
fo37 = '\033[1;37m'

print('Fonte colorida')

print(fo30+'Hello, mundo! 30 cinza')
print(fo31+'Hello, mundo! 31 vermelho')
print(fo32+'Hello, mundo! 32 verde')
print(fo33+'Hello, mundo! 33 amarelo')
print(fo34+'Hello, mundo! 34 azul')
print(fo35+'Hello, mundo! 35 lilás')
print(fo36+'Hello, mundo! 36 azul claro')
print(fo37+'Hello, mundo! 37 branco')

fu40 = '\033[0;40m'
fu41 = '\033[0;41m'
fu42 = '\033[0;42m'
fu43 = '\033[0;43m'
fu44 = '\033[0;44m'
fu45 = '\033[0;45m'
fu46 = '\033[0;46m'
fu47 = '\033[0;47m'

print('\nFundo colorido')

print(fu40+'Hello, mundo! 40 preto')
print(fu41+'Hello, mundo! 41 vermelho')
print(fu42+'Hello, mundo! 42 verde')
print(fu43+'Hello, mundo! 43 amarelo')
print(fu44+'Hello, mundo! 44 azul')
print(fu45+'Hello, mundo! 45 lilás')
print(fu46+'Hello, mundo! 46 azul claro')
print(fu47+'Hello, mundo! 47 cinza')

print('\n\033[1;34;42mFonte e Fundo')
print('\033[1;35;43mHello, mundo!')
