# Operações básicas de dois números informados pelo usuário
import os


def entrada_dados():
    print(f'\n{verde}Operações básicas\n')
    nro1 = int(input('Informe o primeiro número: '))
    nro2 = int(input('\nInforme o segundo número: '))
    return nro1, nro2


def executa_operacoes(nro1, nro2):
    soma = nro1 + nro2
    subtracao = nro1 - nro2
    multiplicacao = nro1 * nro2
    divisao = nro1 / nro2
    return soma, subtracao, multiplicacao, divisao


def imprime_resultado(soma, subtracao, multiplicacao, divisao):
    print(f'\n{branco}A soma {nro1} + {nro2} = {soma:,.0f}'.replace(',','.'))
    print(f'\n{vermelho}A subtração {nro1} - {nro2} = {subtracao:,.0f}'.replace(',','.'))
    print(f'\n{amarelo}A multiplicação {nro1} X {nro2} = {multiplicacao:,.0f}'.replace(',','.'))
    print(f'\n{rosa}A divisão {nro1} / {nro2} = {divisao:.2f}\n'.replace('.',','))


if __name__ == '__main__':
    # definições iniciais
    os.system('cls')
    branco = '\033[0;37m'
    vermelho = '\033[0;31m'
    amarelo = '\033[0;33m'
    rosa = '\033[0;35m'
    verde = '\033[1;32m'
    # pede ao usuário para informar dois números
    nro1, nro2 = entrada_dados()
    soma, subtracao, multiplicacao, divisao = executa_operacoes(nro1, nro2)
    imprime_resultado(soma, subtracao, multiplicacao, divisao)