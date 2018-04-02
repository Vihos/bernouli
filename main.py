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


# def iter_benchmark(args):


def format_output(args, time_):
    roots = args[0]
    iterations = args[1]

    print("Полином степени {0}:".format(len(roots)))

    for i in range(len(roots)):
        print("Корень {0} найден за {1} итераций".format(roots[i], iterations[i]))
    print("Общее время подсчёта: {:5f}мс".format(time_))

    print()


if __name__ == "__main__":
    sys.setrecursionlimit(500)

    # Drawing
    # Построение
    drawing.build_function(f, coefficients0, "f6(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients1, "f5(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients2, "f4(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients3, "f3(x)", -1, 7, -4, 4)
    drawing.build_function(f, coefficients4, "f2(x)", -1, 7, -4, 4)

    drawing.show_plot()

    # Bernoulli benchmark
    bernoulli_time = []

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients0, [6, 5, 4, 3, 2, 1], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients1, [6, 5, 4, 3, 2], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients2, [6, 5, 4, 3], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients3, [6, 5, 4], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)

    start = time.time()
    ret = bernoulli.execute_method_interface(f, coefficients4, [6, 5], accuracy)
    result_time = (time.time() - start) * 1000
    format_output(ret, result_time)
    bernoulli_time.append(result_time)

    # drawing.bar_chart(
    #     [20, 35, 30, 35, 27],
    #     ["Бернулли", "test 2", "test 3", "test 4", "test 5"],
    #     "Производительность",
    #     "Методы",
    #     "Миллисекунды",
    #     graph_params=[0, 51, 5]
    # )

    drawing.data_plot([2, 3, 4, 5, 6], list(reversed(bernoulli_time)),
                      "Рост времени рассчёта от роста степени полинома",
                      "Степень",
                      "Время (мс)",
                      [2, 3, 4, 5, 6, 7])
