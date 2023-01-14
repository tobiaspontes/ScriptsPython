# Operações básicas de dois números informados pelo usuário 
print('\n\033[1;32mOperações básicas'+'\n')
nro1 = int(input('Informe o primeiro número: '))
nro2 = int(input('\nInforme o segundo número: '))
soma = nro1 + nro2
subtracao = nro1 - nro2
multiplicacao = nro1 * nro2
divisao = nro1 / nro2
print(f'\n\033[0;37mA soma dos números é: {soma:}')
print(f'\n\033[0;31mA subtração dos números é: {subtracao:}')
print(f'\n\033[0;33mA multiplicação dos números é: {multiplicacao:}')
print(f'\n\033[0;35mA divisão dos números é: {divisao:.2f}\n')