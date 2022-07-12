import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.rcParams['font.family'] = ['helvetica']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

### Установите квадратичный многочлен
X = np.linspace(-10, 10, 100)
# Y = 4 * X ** 2 - 9 * X + 3 + np.random.randn(100) * 3
Y = -2 * X ** 2 - 9 * X + 3 + np.random.randn(100) * 5


# Стандартная форма квадратичной функции
def secondfun(params, x):
    a, b, c = params
    return a * x * x + b * x + c

# Функция ошибки, то есть разница между значением, полученным с помощью подобранной кривой(,curve fitting) и фактическим значением
def error(params, x, y):
    return secondfun(params, x) - y

# Решите для параметров
# Выведите конечный результат
p0 = [1, 1, 1]## Установите начальный коэффициент и используйте этот метод для решения
Para = leastsq(error, p0, args=(X, Y))## Решать

a, b, c = Para[0]##Отделите коэффициент abc
print('Коэффициент квадратичной функции abc равен:',"a=", a, " b=", b, " c=", c)
#     print("cost:" + str(Para[1]))
plt.scatter(X, Y, color="green",marker='*', label="Точки распределения квадратичных функций", linewidth=2)
#   draw line
x = np.linspace(-10, 10, 100)
y=secondfun(Para[0], x)
plt.plot(x, y, "r-", label="Решающая кривая метода наименьших квадратов", linewidth=2)
plt.legend()  # Нарисуйте легенду
plt.show()


