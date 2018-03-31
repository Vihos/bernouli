# coding=utf-8


# Разностное уравнение (из полинома выражаем х в максимальной степени)
# При каждом вызове нужно сместить коэффициенты приближения вправо
def finite_difference_equation(_coefficients, _approximation):
    result = 0
    length = len(_approximation)

    for n in range(length):
        result += _approximation[n] * _coefficients[n + 1]

    return -result / _coefficients[0]


# принимает: начальное приближение, коэффициенты, номер итерации
# возращает: корень и количество итераций, за которое он найден
def bernoulli_approximation(f, _coefficients, _approximation, _iteration, accuracy=0.1 ** 5):
    x_last = finite_difference_equation(_coefficients, _approximation)
    max_root = x_last / _approximation[0]

    if abs(f(max_root)) <= accuracy:
        return max_root, _iteration
    else:
        _approximation = [x_last] + _approximation[:-1]
        return bernoulli_approximation(f, _coefficients, _approximation, _iteration + 1, accuracy)


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
def execute_method_interface(f, _coefficients, _approximation, accuracy=0.1 ** 5):
    roots = []
    iterations = []
    f_from_roots = []
    length = len(_approximation)

    for k in range(length):
        # 1) approximation of max|root|
        multic = 0.1 ** (length - k - 1)

        temp = bernoulli_approximation(f, _coefficients, _approximation, 0, accuracy * multic)

        roots.append(temp[0])
        iterations.append(temp[1])
        f_from_roots.append(f(temp[0]))

        # 2) creation new polynomial coefficients
        _coefficients = gornor_schema(_coefficients, temp[0])
        # delete one approximation
        _approximation.remove(_approximation[0])
    return roots, iterations, f_from_roots
