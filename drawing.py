import matplotlib.pyplot as plt
import numpy as np

import datetime
import random

# Промежутки отрисовки функции
START_X = -10
END_X = 10
START_Y = -8
END_Y = 5


# Строит функцию f(x)
# принимает:
# func - функция от одного параметра
# argument - коэффициенты полинома
# legend - подпись
# x_from - начало отрисовки функции по х
# x_to - конец отрисовки функции по х
# y_from - начало отрисовки функции по y
# y_to - конец отрисовки функции по y
# dx - шаг отрисовки, Стандартно 0.01
def build_function(func, argument=None, legend="", x_from=START_X, x_to=END_X, y_from=START_Y, y_to=END_Y, dx=0.01):
    plt.axis([x_from, x_to, y_from, y_to])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    x = np.arange(x_from, x_to, dx)

    if len(legend) > 0:
        if argument is not None:
            plt.plot(x, func(x, argument), label=legend)
        else:
            plt.plot(x, func(x), label=legend)

        plt.legend()
    else:
        if argument is not None:
            plt.plot(x, func(x, argument))
        else:
            plt.plot(x, func(x))


# Отрисовывает функции, которые были построены через 'build_function(...)'
def show_plot():
    plt.show()


def bar_chart(values_array, values_names=None, title=None, x_title=None, y_title=None, graph_params=None):
    ind = np.arange(len(values_array))
    width = 0.35

    p = plt.bar(ind, values_array, width)

    if title is not None:
        plt.title(title)

    if x_title is not None:
        plt.xlabel(x_title)

    if y_title is not None:
        plt.ylabel(y_title)

    if values_names is not None and len(values_names) == len(values_array):
        plt.xticks(ind, values_names)

    if graph_params is not None and len(graph_params) == 3:
        plt.yticks(np.arange(graph_params[0], graph_params[1], graph_params[2]))

    plt.show()


def data_plot(x, y, legend, title=None, x_title=None, y_title=None, xticks=None):
    if title is not None:
        plt.title(title)

    if x_title is not None:
        plt.xlabel(x_title)

    if y_title is not None:
        plt.ylabel(y_title)

    if xticks is not None:
        plt.xticks(xticks)

    plt.plot(x, y, label=legend)
    plt.legend()
