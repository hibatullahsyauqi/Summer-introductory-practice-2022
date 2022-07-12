#from math import *

#projtitle = '''Вычисление первой производной функции f(x) = sin(x)
#методом правых конечных разностей для
#различного расстояния между узлами (сетками)'''
#print(projtitle)

# Вычисление приближенной производной
#def diff(x, h):
#   return (sin(x + h) - sin(x)) / h

#def difff(x):
#   return cos(x)

#x = 1

# Вычисление погрешность производной при разных h
#for i in range(1, 8):
#   h = float(0.1 ** i)
#   print('\nрасстояние между узлами (сетками): ', round(h, 8))
#   print('приближенная производная: ', diff(x, h))
#   print("производная для f(x) = sin(x)    ->   f'(x) = cos(x): ", difff(x))
#   print('погрешность: ', abs(diff(x, h) - difff(x)))
#   i += 1
###

from math import *

projtitle = '''Вычисление первой производной функции f(x) = sin(x)
методом центральных конечных разностей для
различного расстояния между узлами (сетками)'''
print(projtitle)

# Вычисление приближенной производной
def diff(x, h):
    return (sin(x + h) - sin(x-h)) / (2*h)

def difff(x):
    return cos(x)

x = 1

# Вычисление погрешность производной при разных h
for i in range(1, 8):
    h = float(0.1 ** i)
    print('\nрасстояние между узлами (сетками): ', round(h, 8))
    print('приближенная производная: ', diff(x, h))
    print("производная для f(x) = sin(x)    ->   f'(x) = cos(x): ", difff(x))
    print('погрешность: ', abs(diff(x, h) - difff(x)))
    i += 1
