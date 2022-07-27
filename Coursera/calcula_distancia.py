# Este código pede ao usuário para informar as coodernadas de dois pontos,
# e calcula a distância entre eles.

import math

def calcula_distancia(x1,y1,x2,y2):
	return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


if (__name__ == '__main__'):
	x1 = float(input('\nDigite a abcissa do primeiro ponto: '))
	y1 = float(input('Digite a ordenada do primeiro ponto: '))
	x2 = float(input('Digite a abcissa do segundo ponto: '))
	y2 = float(input('Digite a ordenada do segundo ponto: '))
	distancia = calcula_distancia(x1,y1,x2,y2)
	print(f'\nA distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é de {distancia:.2f}.')