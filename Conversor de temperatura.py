# Conversor de Unidades: Graus Celsius e Fahrenheit

branco = '\033[0;29m'
preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
rosa = '\033[0;35m'
azul = '\033[0;36m'
cinza = '\033[0;37m'

def menu_inicial():
   print('\n',verde,'Programa para Conversão de Temperaturas', sep='')
   print('\n(1) Celsius para Fahrenheit   (2) Fahrenheit para Celsius')

def cel_fahr():
   C = float(input('\nEntre com a temperatura em graus Celsius: '))
   F = C * (9 / 5) + 32
   print(azul,'Valor em Fahrenheit: {0:.2f}°F'.format(F),sep='')

def fahr_cel():
   F = float(input('\nEntre com a temperatura em graus Fahrenheit: '))
   C = (F - 32) * (5 / 9)
   print(azul,'Valor em Celsius: {0:.2f}°C'.format(C),sep='')

if __name__=='__main__':
   menu_inicial()
   escolha = input('\nEscolha o tipo de conversão: ')
   if escolha == '1':
      cel_fahr()
   if escolha == '2':
      fahr_cel()