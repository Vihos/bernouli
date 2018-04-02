from decimal import *


def lobachevsky_method(f, coefficients, coefficients_, iterations, accuracy=0.1 ** 5):
    temp = dict()
    length_c = len(coefficients)

    iter_power = 1 / 2 ** (iterations - 1)

    accuracy_check = True
    for i in range(length_c - 1):
        if i + 1 < length_c:
            temp[i] = (coefficients[i + 1] / coefficients[i]) ** iter_power

            if abs(f(temp[i], coefficients_)) > accuracy and abs(f(-temp[i], coefficients_)) > accuracy:
                accuracy_check = False

    if accuracy_check:
        acc_f = dict()

        for i in range(length_c - 1):
            if abs(f(temp[i], coefficients_)) >= accuracy:
                temp[i] = -temp[i]
                acc_f[i] = f(temp[i], coefficients_)

        return [temp, iterations, acc_f]

    b = dict()

    for i in range(length_c):
        if i == 0 or i == length_c - 1:
            b[i] = coefficients[i] ** 2
        else:
            b[i] = coefficients[i] ** 2 - 2 * coefficients[i - 1] * coefficients[i + 1]

    return lobachevsky_method(f, b, coefficients_, iterations + 1, accuracy)


def lobachevsky_execute(f, coefficients, accuracy=0.1 ** 5):
    return lobachevsky_method(f, coefficients, coefficients, 1, accuracy)
