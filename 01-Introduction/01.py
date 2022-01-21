import math


def f(x):
    return math.sqrt(x + 3) - x + 1


def g(t):
    return t ** 2 - 1


def h(x):
    return x ** 2 + 1 / x + 2


# list of values to plug in
for x in [0, 1, math.sqrt(2), math.sqrt(2) - 1]:
    print("f({:.3f}) = {:.3f}".format(x, f(x)))


# # list of values to plug in
# for x in [0, 1, math.sqrt(2), math.sqrt(2) - 1]:
#     print("f({:.3f}) = {:.3f}".format(x, g(t))
#
#
# # list of values to plug in
# for x in [0, 1, math.sqrt(2), math.sqrt(2) - 1]:
#     print("f({:.3f}) = {:.3f}".format(x, h(x)))
