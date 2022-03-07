l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

k = 1
while a >= k:
    i = 1
    while l >= i:
        print('#', end = '')
        i = i + 1
    print()
    k = k + 1
