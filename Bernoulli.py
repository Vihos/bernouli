# coding=utf-8

import sys
import time
import warnings
import drawing as dr

# Constants
# Константы
accuracy = 0.1 ** 3

# Coefficients of a polynomial
# Коэффициенты полинома
coefficients = [1, -15, 85, -225, 274, -120, -2]


# The polynomial at the point
# Полином в точке
def f(point, a=coefficients):
    result = 0
    power = len(a)

    for n in range(0, power):
        result += a[n] * point ** (power - n - 1)

    return result


# Разностное уравнение (из полинома выражаем х в максимальной степени)
# При каждом вызове нужно сместить коэффициенты приближения
# TODO Rename
def x_max_degree(_coefficients, _approximation):
    # print(_approximation)
    # print(_coefficients)
    result = 0
    length = len(_approximation)

    for n in range(length):
        # print(n)
        result += _approximation[n] * _coefficients[n + 1]

    return -result / _coefficients[0]


# принимает: начальное приближение, коэффициенты, номер итерации
# возращает: корень и количество итераций, за которое он найден
def bernoulli_approximation(_coefficients, _approximation, _iteration):
    print(_iteration)
    print(_coefficients)
    print(_approximation)
    x_last = x_max_degree(_coefficients, _approximation)
    max_root = x_last / _approximation[0]
    print(max_root)
    print(f(max_root))
    print()
    multic = len(_approximation)
    print(multic)
    print()

    if abs(f(max_root)) <= accuracy * 0.1 ** (multic - 1):
        return max_root, _iteration
    else:
        _approximation = [x_last] + _approximation[:-1]
        return bernoulli_approximation(_coefficients, _approximation, _iteration + 1)


# принимает: коэффициенты полинома, корень
# возращает: новые коэффициенты полинома
def gornor_schema(_coefficients, root):
    new_coefficients = [_coefficients[0]]

    length = len(_coefficients) - 2

    for n in range(length):
        new_coefficients.append(root * new_coefficients[n] + _coefficients[n + 1])

    return new_coefficients


# 2 steps: 1) approximation of max|root| 2) creation new polynomial coefficients
# принимает: начальное приближение, коэффициенты
def bernoulli_method_interface(_coefficients, _approximation):
    # print(_coefficients)
    # print(_approximation)
    roots = []
    iterations = []
    f_from_roots = []
    length = len(_approximation)

    for k in range(length):
        # 1) approximation of max|root|
        temp = bernoulli_approximation(_coefficients, _approximation, 0)

        roots.append(temp[0])
        iterations.append(temp[1])
        f_from_roots.append(f(temp[0]))

        print(roots)
        print(iterations)
        print(f_from_roots)
        print()

        # 2) creation new polynomial coefficients
        _coefficients = gornor_schema(_coefficients, temp[0])
        _approximation.remove(_approximation[0])  # delete one approximation
    return roots, iterations, f_from_roots


if __name__ == "__main__":
    dr.build_function(f,
                      coefficients,
                      "Первая функция системы",
                      )

    dr.show_plot()

    print(bernoulli_method_interface(coefficients, [1, 1, 2, 1, 2, 1]))

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
