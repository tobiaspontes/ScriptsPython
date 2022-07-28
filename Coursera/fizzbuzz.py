def fizzbuzz(n):
    y = n % 3
    w = n % 5
    if y == 0:
        if w == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    else:
        if w == 0:
            return 'Buzz'
        else:
            return n


if (__name__ == '__main__'):
    x = int(input('\nDigite um número inteiro: '))
    if fizzbuzz(x) == 'FizzBuzz':
        print(f'\nO número {x:,.0f} é divisível por 3 e 5.\n'.replace(',','.'))
    if fizzbuzz(x) == 'Fizz':
        print(f'\nO número {x:,.0f} é divisível por 3.\n'.replace(',','.'))
    if fizzbuzz(x) == 'Buzz':
        print(f'\nO número {x:,.0f} é divisível por 5.\n'.replace(',','.'))
    if fizzbuzz(x) == x:
        print(f'\nO número {x:,.0f} não é divisível por 3 nem por 5.\n'.replace(',','.'))

