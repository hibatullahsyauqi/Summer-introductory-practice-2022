from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mplt
from scipy.optimize import leastsq

myfonts = "Times New Roman"
mplt.rcParams['font.family'] = "sans-serif"
mplt.rcParams['font.sans-serif'] = myfonts
mplt.rcParams['axes.unicode_minus'] = False

### Установление квадратичного многочлена
X = np.linspace(-10, 10, 100)
Y = np.random.randn(100) * (X ** 2) + np.random.randn(100) * X + np.random.randn(100)
# Y = -2 * X ** 2 - 9 * X + 3 + np.random.randn(100) * 5


# Стандартная форма квадратичной функции
def secondfun(params, x):
    a, b, c = params
    return a * x * x + b * x + c


# Функция ошибки, то есть разница между значением, полученным с помощью подобранной кривой(,curve fitting) и фактическим значением
def error(params, x, y):
    return secondfun(params, x) - y


# Решение для параметров
# Вывод конечного результата
p0 = [1, 1, 1]  ##Установление начального коэффициента и использование этого метода для решения
Para = leastsq(error, p0, args=(X, Y))  ##Решение

a, b, c = Para[0]  ##Коэффициента abc
print('Коэффициент квадратичной функции abc равен:', "a=", a, " b=", b, " c=", c)
#   print("cost:" + str(Para[1]))
plt.scatter(X, Y, color="blue", marker='o', label="Точки распределения квадратичных функций", linewidth=1)
#   draw line
x = np.linspace(-10, 10, 100)
y = secondfun(Para[0], x)
plt.plot(x, y, "r-", label="Решающая кривая метода наименьших квадратов", linewidth=1)
plt.legend()  # Вывод легенду
plt.show()
