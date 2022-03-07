x1 = float(input('Digite a abcissa do primeiro ponto: '))
y1 = float(input('Digite a ordenada do primeiro ponto: '))
x2 = float(input('Digite a abcissa do segundo ponto: '))
y2 = float(input('Digite a ordenada do segundo ponto: '))
import math
distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
if distancia >= 10:
	print('longe')
else:
	print('perto')