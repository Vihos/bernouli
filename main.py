# coding=utf-8

import sys
import time
import drawing
import bernoulli

# Constants
# Константы
accuracy = 0.1 ** 5

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients0 = [1, -15, 85, -225, 274, -120]
coefficients1 = [1, -10, 35, -50, 24]
coefficients2 = [1, -6, 11, -6]
coefficients3 = [1, -3, 2]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients0):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


if __name__ == "__main__":
    sys.setrecursionlimit(500)

    # Drawing
    # Построение
    drawing.build_function(f, coefficients0, "f5(x)", -1, 6, -4, 4)
    drawing.build_function(f, coefficients1, "f4(x)", -1, 6, -4, 4)
    drawing.build_function(f, coefficients2, "f3(x)", -1, 6, -4, 4)
    drawing.build_function(f, coefficients3, "f2(x)", -1, 6, -4, 4)

    drawing.show_plot()

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients0, [5, 4, 3, 2, 1], 0.1 ** 5))
    end = time.time()
    print('{:f}'.format(end - start))

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients1, [5, 4, 3, 2], 0.1 ** 5))
    end = time.time()
    print('{:f}'.format(end - start))

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients2, [5, 4, 3], 0.1 ** 5))
    end = time.time()
    print('{:f}'.format(end - start))

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients3, [5, 4], 0.1 ** 5))
    end = time.time()
    print('{:f}'.format(end - start))

    # mpl.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернулли", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )

    # start = time.time()
    # end = time.time()
    # print('{:f}'.format(end - start))
