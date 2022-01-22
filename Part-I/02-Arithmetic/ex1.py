"""
Page 34
Find the sum of alll the numbers from 1 to 100. How about from 1 to 1,1000?
See a pater?
"""


def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


print(summation(10))
print()
print(summation(100))
print()
print((summation(1000)))
