''' Tabela de temperatura Fahrenheit X Celsius '''

Fahrenheit = -270
while Fahrenheit <= 500:
    print(Fahrenheit, 'Fahrenheit =', round((Fahrenheit - 32) * 5 / 9, 2), 'Celsius')
    Fahrenheit = Fahrenheit + 10
