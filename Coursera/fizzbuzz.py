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
