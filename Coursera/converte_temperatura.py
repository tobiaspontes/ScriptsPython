# Este código converte temperatura entre Celsius e Fahrenheit.

def mensagem_inicial():
    print()
    print(55 * '*')
    print('*         C = converte Fahrenheit em Celsius          *')
    print('*', 51 * ' ', '*')
    print('*         F = converte Celsius em Farhrenheit         *')
    print(55*'*')

# Conversor de temperatura Fahrenheit em Celsius
def fahrenheit_pra_celsius(temperatura_fahrenheit):
    temperatura_celsius = (float(temperatura_fahrenheit) - 32) * 5 / 9
    return temperatura_celsius

# Conversor de temperatura Celsius em Fahrenheit
def celsius_pra_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = float(temperatura_celsius) * 9 / 5 + 32
    return temperatura_fahrenheit

if (__name__ == '__main__'):
    mensagem_inicial()
    opcao = input('\nDigite "C" para converter para Celsius, "F" para converter para Fahrenheit ou Enter para sair: ')
    if (opcao == 'C'):
        temperatura_fahrenheit = input('Digite a temperatura em Fahrenheit: ')
        temperatura_celsius = fahrenheit_pra_celsius(temperatura_fahrenheit)
        print(f'A temperatura em Celsius é {temperatura_celsius:.1f}')
    elif (opcao == 'F'):
        temperatura_celsius = input('Digite a temperatura em Celsius: ')
        temperatura_fahrenheit = celsius_pra_fahrenheit(temperatura_celsius)
        print(f'A temperatura em Fahrenheit é {temperatura_fahrenheit:.1f}')
    else:
        pass
