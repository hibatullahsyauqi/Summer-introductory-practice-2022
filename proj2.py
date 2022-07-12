#from math import *

#a = 0
#b = 1
#def f(x):
#    return exp(x)
#def integrall(a, b):
#    return exp(b)-exp(a)
#def integral(a, b, h):
#    s = 0.0
#    while a <= b:
#        s += f(a)*h
#        a += h
#    return s

#for i in range(1,8):
#    h = float(0.1 ** i)
#    print('\nДлина отрезка', round(h, 8))
#    print('Приближенный интеграл', integral(a, b, h))
#    print('Интеграл для f(x) = exp(x)   ->     F(x) = exp(x): ', integrall(a, b))
#    print('Погрешность: ', abs(integral(a, b, h)-integrall(a, b)))
#    i += 1

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
        def mid(a, h):
            return (2 * a + h) / 2
        s += f(mid(a, h))*h
        a += h
    return s

for i in range(1,7):
    h = float(0.1 ** i)
    print('\nДлина отрезка', round(h, 7))
    print('Приближенный интеграл', integral(a, b, h))
    print('Интеграл для f(x) = exp(x)   ->     F(x) = exp(x): ', integrall(a, b))
    print('Погрешность: ', abs(integral(a, b, h)-integrall(a, b)))
    i += 1

