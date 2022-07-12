from math import *


def func(x):
    return cos(x)


def diff(x, h, func):
    return (func(x + h) - func(x - h)) / (2 * h)


def runge(epsilon, func, h, x):
    h1 = h
    print("начальный шаг = %.20f" % (h1))
    h2 = h1 / 2
    print("начальный половинный шаг = %.20f" % (h2))
    dif1 = (func(x + h1) - func(x - h1)) / (2 * h)
    dif2 = (func(x + h2) - func(x - h2)) / (2 * h)
    differential = abs(dif1 - dif2)
    err = differential / 3
    print("ошибка = %.20f" % (err))
    while err > epsilon:
        h1 = h2
        h2 = h1 / 2
        dif1 = (func(x + h1) - func(x - h1)) / (2 * h)
        dif2 = (func(x + h2) - func(x - h2)) / (2 * h)
        differential = abs(dif1 - dif2)
        if err < differential / 3:
            print("запрошенная точность недостижима")
            print("предельная точность при шаге равном == %.20f" % (h2 * 2))
            print("%24.18f - соотвествующее значение производной" % (err))
            return 0
            break
        else:
            err = differential / 3
    print("%.18f - шаг для заданной точности" % (h2))
    print("%.18f - производная" % (dif2))
    print("%.18f - ошибка" % (err))
    return 0


print("производная для функции cos(x) ")
print("введите шаг: ")
a = float(input())
print("введите допустимая погрешность: ")
b = float(input())
print("введите точку: ")
c = float(input())
runge(b, func, a, c)
