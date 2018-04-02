def lobachevsky_method(f, coefficients, iterations, accuracy=0.1 ** 5):
    if iterations > 0:

        temp_x1 = (coefficients[1] / coefficients[0]) ** (1 / 2 ** (iterations - 1))
        temp_x2 = (coefficients[2] / coefficients[1]) ** (1 / 2 ** (iterations - 1))
        temp_x3 = (coefficients[3] / coefficients[2]) ** (1 / 2 ** (iterations - 1))

        if (abs(f(temp_x1, coefficients)) <= accuracy or (f(-temp_x1, coefficients)) <= accuracy) and (
                abs(f(temp_x2, coefficients)) <= accuracy or (f(-temp_x2, coefficients)) <= accuracy) and (
                abs(f(temp_x3, coefficients)) <= accuracy or (f(-temp_x3, coefficients)) <= accuracy):

            if abs(f(temp_x1, coefficients)) >= accuracy:
                temp_x1 = -temp_x1

            if abs(f(temp_x2, coefficients)) >= accuracy:
                temp_x2 = -temp_x2

            if abs(f(temp_x3, coefficients)) >= accuracy:
                temp_x3 = -temp_x3

            return [[temp_x1, temp_x2, temp_x3], iterations, [f(temp_x1, coefficients), f(temp_x2, coefficients), f(temp_x3, coefficients)]]

    b0 = coefficients[0] ** 2
    b1 = coefficients[1] ** 2 - 2 * coefficients[0] * coefficients[2]
    b2 = coefficients[2] ** 2 - 2 * coefficients[1] * coefficients[3]
    b3 = coefficients[3] ** 2

    coefficients = [b0, b1, b2, b3]

    return lobachevsky_method(f, coefficients, iterations + 1, accuracy)


def lobachevsky_execute(f, coefficients, accuracy=0.1 ** 5):
    return lobachevsky_method(f, coefficients, 1, accuracy)
