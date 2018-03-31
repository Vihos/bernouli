# coding=utf-8

import sys
import time
import warnings
import drawing as dr
import bernoulli

# Constants
# Константы
accuracy = 0.1 ** 5

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients = [1, -15, 85, -225, 274, -120]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


if __name__ == "__main__":
    dr.build_function(f,
                      coefficients,
                      "Первая функция системы",
                      -1, 6,
                      -4, 4
                      )

    dr.show_plot()

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients, [1, 1, 2, 1, 2], 0.1**5))
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
