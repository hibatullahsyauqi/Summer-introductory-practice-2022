from math import *

a = 0
b = 1
def f(x):
    return exp(x)
def integrall(a, b):
    return exp(b)-exp(a)
def integral(a, b, h):
    s = 0.0
    while a <= b:
        s += f(a)*h
        a += h
    return s

for i in range(1,8):
    h = float(0.1 ** i)
<<<<<<< HEAD
    print('\nДлина отрезка', round(h, 8))
=======
    print('\nРасстояние между узлами (сетками)', round(h, 8))
>>>>>>> origin/main
    print('Приближенный интеграл', integral(a, b, h))
    print('Интеграл для f(x) = exp(x)   ->     F(x) = exp(x): ', integrall(a, b))
    print('Погрешность: ', abs(integral(a, b, h)-integrall(a, b)))
    i += 1

