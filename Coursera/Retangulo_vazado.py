l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

k = 1
while a >= k:
    if k == 1 or k == a:
        i = 1
        while l >= i:
            print('#', end = '')
            i = i + 1
    else:
        i = 1
        while l >= i:
            if i == 1 or i == l:
                print('#', end = '')
            else:
                print(' ', end = '')
            i = i + 1
    print()
    k = k + 1
