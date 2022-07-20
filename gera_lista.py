# a classe Lista gera uma lista de números inteiros aleatórios dentro de um intervalo

class Lista:
    def __init__(self, n, li, ls):
        intervalo = (ls + 1) - li
        if (intervalo <= 0):
            print('Erro! Limite superior deve ser maior do que limite inferior!')
            exit()
        if (n > intervalo):
            print('Erro! Quantidade de números solicitados maior do que o intervalo!')
            exit()
        import random
        self.lista = []
        i = 1
        while i <= n:
            numero = random.randrange(li, ls + 1)
            self.lista.append(numero)
            i += 1
