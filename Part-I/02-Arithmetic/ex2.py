"""
Page 35
Find the average of the numbers in the list below:

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]
"""


def average_of_numbers_in_list(list):
    total = 0
    for i in list:
        total += i
    return total/len(list)


d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]
print(average_of_numbers_in_list(d))
