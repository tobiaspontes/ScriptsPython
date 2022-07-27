def mensagem_inicial():
    print()
    print(55 * '*')
    print('*   S = converte segundos em dias, horas e minutos    *')
    print('*', 51 * ' ', '*')
    print('*   D = converte dias, horas e minutos em segundos    *')
    print(55*'*')

# O usuário informa a quantidade de segundos e o código converte em dias, horas, minutos e segundos

def converte_segundos():
    segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')
    total_segs = int(segundos_str)
    dias = total_segs // 86400 # cada dia tem 86400 segundos; o número inteiro da divisão é a qtde de dias
    segs_restantes1 = total_segs % 86400 # aqui é calculado o resto da divisão (dia fracionário)
    horas = segs_restantes1 // 3600 # a hora tem 3600 segundos; o número inteiro da divisão é quantidade de horas
    segs_restantes2 = segs_restantes1 % 3600 # o resto da divisão é a qtde fracionária de horas
    minutos = segs_restantes2 // 60 # o minuto tem 60 segundos; o inteiro da divisão é a qtde de minutos
    segundos = segs_restantes2 % 60 # o resto da divisão é quantidade de segundos (minuto fracionário)
    print('\n', dias, 'dias,', horas, 'horas,', minutos, 'minutos e',segundos, 'segundos.')

# O usuário informa a quantidade de dias, horas e minutos e o código converte em segundos

def converte_dias():
    dias = int(input('Quantos dias? '))
    horas = int(input('Quantas horas? '))
    minutos = int(input('Quantos minutos? '))
    total_segundos = 86400 * dias + 3600 * horas + 60 * minutos
    print(f'\nO total de segundos é: {total_segundos:,}.'.replace(',','.'))

if (__name__ == '__main__'):
    mensagem_inicial()
    opcao = input('\nDigite "S" se deseja converter segundos, ou "D" se deseja converter dias: ')
    if opcao == 'S':
        converte_segundos()
    elif opcao == 'D':
        converte_dias()
    else:
        print('\nOpçao desconhecida!')
                    
