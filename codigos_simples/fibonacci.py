import os

os.system('cls')

# Definir uma função para gerar a sequência de Fibonacci
def fibonacci(n):
  # Inicializar as duas primeiras variáveis da sequência
  a = 0
  b = 1
  # Criar uma lista vazia para armazenar os termos da sequência
  lista = []
  # Usar um laço for para iterar n vezes
  for i in range(n):
    # Adicionar o valor de a à lista
    lista.append(a)
    # Atualizar os valores de a e b usando a regra de Fibonacci
    a, b = b, a + b
  # Retornar a lista com os termos da sequência
  return lista

# Testar a função com um exemplo
n = int(input('\nInforme o números de elementos da sequência de Fibonacci: '))
print(f'\nSequência de Fibonacci para {n} elementos: {fibonacci(n)}\n')