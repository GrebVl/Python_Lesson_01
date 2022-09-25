# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

xCordinatPoint1 = int(input('Введите кординату X точки 1: '))
yCordinatPoint1 = int(input('Введите кординату Y точки 1: '))

xCordinatPoint2 = int(input('Введите кординату X точки 2: '))
yCordinatPoint2 = int(input('Введите кординату Y точки 2: '))


distanceBeetweenPoint = math.sqrt(pow(xCordinatPoint1 - xCordinatPoint2, 2) + pow(yCordinatPoint1 - yCordinatPoint2, 2))

print('растояние между точками равно: ', round(distanceBeetweenPoint, 3))