"""
Python program to test the arithmetic skill
@varunjha089
"""


def average(a, b):
    return (a + b) / 2


print(average(5, 9))


def summation(num):
    running_sum = 0
    for i in range(1, num + 1):
        running_sum += i
    return running_sum


print(summation(10))
