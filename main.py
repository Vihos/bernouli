# coding=utf-8

import sys
import time
import drawing
import bernoulli

# Constants
# Константы
accuracy = 0.1 ** 6

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients0 = [1, -21, 175, -735, 1624, -1764, 720]
coefficients1 = [1, -15, 85, -225, 274, -120]
coefficients2 = [1, -10, 35, -50, 24]
coefficients3 = [1, -6, 11, -6]
coefficients4 = [1, -3, 2]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients0):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


if __name__ == "__main__":
    sys.setrecursionlimit(2000)

    # Drawing
    # Построение
    drawing.build_function(f, coefficients0, "f6(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients1, "f5(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients2, "f4(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients3, "f3(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients4, "f2(x)", -1, 7, -4, 4)

    drawing.show_plot()

    result_time = []

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients0, [6, 5, 4, 3, 2, 1], accuracy))
    end = time.time()
    result_time.append(end - start)

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients1, [6, 5, 4, 3, 2], accuracy))
    end = time.time()
    result_time.append(end - start)

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients2, [6, 5, 4, 3], accuracy))
    end = time.time()
    result_time.append(end - start)

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients3, [6, 5, 4], accuracy))
    end = time.time()
    result_time.append(end - start)

    start = time.time()
    print(bernoulli.execute_method_interface(f, coefficients4, [6, 5], accuracy))
    end = time.time()
    result_time.append(end - start)

    # drawing.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернулли", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )

    drawing.data_plot([2, 3, 4, 5, 6], list(reversed(result_time)),
                      "Рост времени рассчёта от роста степени полинома",
                      "Степень",
                      "Время",
                      [2, 3, 4, 5, 6, 7])
