# Conversor de Unidades: Graus Celsius e Fahrenheit

def menu_inicial():
   print('\n\033[1;32mPrograma para Conversão de Temperaturas')
   print('\n1. Converter de Celsius para Fahrenheit')
   print('\n2. Converter de Fahrenheit para Celsius')

def cel_fahr():
   C = float(input('\nEntre com a temperatura em graus Celsius: '))
   F = C * (9 / 5) + 32
   print('\n\033[0;36mValor em Fahrenheit: {0:.2f}°F\n'.format(F))

def fahr_cel():
   F = float(input('\nEntre com a temperatura em graus Fahrenheit: '))
   C = (F - 32) * (5 / 9)
   print('\n\033[0;36mValor em Celsius: {0:.2f}°C\n'.format(C))

if __name__=='__main__':
   menu_inicial()
   escolha = input('\nEscolha o tipo de conversão: ')
   if escolha == '1':
      cel_fahr()
   if escolha == '2':
      fahr_cel()