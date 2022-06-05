import numpy as np

a = np.array([3, 5, 1, 2])

i_max = a.argmax()
i_min = a.argmin()

print(f'O índice do maior argumento é: {i_max}')
print(f'O índice do menor argumento é {i_min}')

print(f'O valor do maior argumento é: {a[i_max]}')
print(f'O valor do menor argumento é: {a[i_min]}')